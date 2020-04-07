# -*- coding: utf-8 -*-
import os
import sys
import time
from pprint import pprint
from fundata.request import ApiClient
from fundata.client import init_api_client

#unit test api
from fundata.dota2.match import get_batch_basic_info
from fundata.dota2.match import get_single_basic_info
from fundata.dota2.player.player_info import get_batch_player
from fundata.dota2.player.player_detail import get_player_detail_stats,get_player_data_status
#unit test mysql
from mysql.sqlConnect import sqlConnection,sqlDisconnection,sqlSelect, sqlInsert
from mysql.dataHandler import api_transfer_sql




#print(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def test():
    cur=sqlConnection()
    res=sqlSelect("SELECT id FROM player WHERE name<>%s limit 1","x")
    init_api_client()
    for everyOne in res:
        status = get_player_data_status(everyOne[0])
        if status==2: 
            print("find one=%i"%everyOne[0])
            get_player_detail_stats(everyOne[0])

    sqlDisconnection()


# 测试获取批量比赛基本数据
def test_single_basic_info():
    # FIXME，需要设置 public_key/secret_key
    init_api_client()

    res = get_single_basic_info(3766730668)
    pprint(res)

    """DONE***
    res=get_batch_player(0,3000)
    row=sqlInsert("insert into player(id, real_name, name, nation, position) values (%s, %s, %s, %s, %s)",param)
    """

def sql():
    #将数据插入mysql
    cur=sqlConnection()
   
    res=sqlSelect("SELECT id FROM player WHERE name<>%s","x")
    #res=sqlInsert("insert into lobby_type( en_name, cn_name) values (%s,%s)", [('test22','2'),('test23','3')])
    #res=sqlInsert("insert into lobby_type( en_name, cn_name) values (%s,%s)", [('test22','2')])
    sqlDisconnection()


def sync_match(s_time,volume):
    """从api多次读取match信息，并且插入mysql数据库
    参数：s_time是str，例如"2020-1-1 00:00:00"；limit是int，需要数据条数
    返回：影响行数，未写完
    """
    if volume<=0: return 0
    #转化时间为时间戳，设置初始值
    start_time=int(time.mktime(time.strptime(s_time, "%Y-%m-%d %H:%M:%S")))
    start_from=0
    limit=200
    
    #初始化api和mysql，新建参数变量
    init_api_client()
    param=[]
    cur=sqlConnection()
    sql="insert "

    while volume//limit>0: #当获取数据条数总数，大于api上限时，分批请求
        res=get_batch_basic_info(start_time,start_from,limit)
        param=param+api_transfer_sql(res) #将api的返回值转化为mysql需要的参数，并且拼接起来
        #print("start=%s, volume=%s, param len=%i"%(start_from,volume,len(param)))
        volume=volume-limit
        start_from=res["data"][len(res["data"])-1]["match_id"] #获取最后一个match_id作为下一次api请求的参数，接着请求
    else:
        if volume==0: return len(param) #总数是上限的倍数，分批请求完成

        #print("Last Time=%i"%volume)
        #res=[]
        res=get_batch_basic_info(start_time,start_from,volume)#剩余总数<上限，最后一次请求
        #****当超过limit之后，上层多回复了一条数据????****
        #print(res)
        param=param+api_transfer_sql(res) #分批请求完成
       # print("start=%s, volume=%s, param len=%i"%(start_from,volume,len(param)))
    
    return len(param)
    #print(param)
        


if __name__ == "__main__":

   #sync_match("2020-1-1 00:00:00",9)
   test()
   """
   init_api_client()
   res=get_player_detail_stats(101695162)
   print(res)
   """







    
