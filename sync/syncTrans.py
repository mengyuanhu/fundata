#调用别的文件夹中py时使用
import os
import sys
current_dir = os.getcwd()    # obtain work dir
sys.path.append(current_dir) # add work dir to sys pat

import time
from fundata.client import init_api_client
from fundata.dota2.league.league import *
from fundata.dota2.league.player import *
from fundata.dota2.league.team import *
from fundata.dota2.match.match import *
from fundata.dota2.raw.raw import *

from mysql.sqlConnect import *
from mysql.dataHandler import *

def sync_match(s_time,volume):
    """从api多次读取match信息，并且插入mysql数据库
    参数：s_time是str，例如"2020-1-1 00:00:00"；limit是int，需要数据条数
    返回：影响行数
    """
    if volume<=0: return 0
    #转化时间为时间戳，设置初始值
    start_time=int(time.mktime(time.strptime(s_time, "%Y-%m-%d %H:%M:%S")))
    start_from=0
    limit=200 #API接口请求的最大限额
    
    #初始化api和mysql，
    init_api_client()
    sqlConnection()


    #新建插入Sql语句变量
    param=[]
    sql=[]
    while volume//limit>0: #当获取数据条数总数，大于api上限时，分批请求
        res=get_batch_basic_info(start_time,start_from,limit)
        param=param+api_transfer_sql(res) #将api的返回值转化为mysql需要的参数，并且拼接起来
        print("start=%s, volume=%s, param len=%i"%(start_from,volume,len(param)))
        volume=volume-limit
        start_from=res["data"][len(res["data"])-1]["match_id"] #获取最后一个match_id作为下一次api请求的参数，接着请求
    else:
        if volume!=0: #总数不是上限的倍数，剩余总数<上限，最后一次请求
            res=get_batch_basic_info(start_time,start_from,volume)#****当超过limit之后，Fundata的API回复了一条数据****
            param=param+api_transfer_sql(res) #分批请求完成
            print("start=%s, volume=%s, param len=%i"%(start_from,volume,len(param)))
        
    #再请求一条数据，组成sql语句
    res_a=get_batch_basic_info(start_time,start_from,1)
    sql="insert into match_basic("+sqlColumn(res_a)["key"]+") values ("+sqlColumn(res_a)["s"]+")"

    #执行插入
    row=sqlInsert(sql,param)
    #关闭数据库
    sqlDisconnection()
    return row

def sync_team(volume):
    """将API获取到的战队基本信息，不强制新建表并且储存到数据库中
    参数：volume=[int] 队员数量
    返回：数据库影响行数
    """
    if volume<=0: return 0 #参数无效，返回

    ##从API拿数据
    init_api_client()
    res=get_batch_team(0,volume)
    if fetch_data(res)==0: return 0 #未获取到API数据，返回
    
    ##写入MySQL
    sqlConnection()
    if createTable("team",res)==0: return 0 #建表失败，返回
    
    #将API返回结果，转化成参数
    param=api_transfer_sql(res)
    #插入数据
    str=sqlColumn(res)
    sql="insert into team("+str["key"]+") values ("+str["s"]+")"
    row=sqlInsert(sql,param)
    
    #关闭数据库
    sqlDisconnection()
    return row

def sync_player(volume):
    """将API获取到的队员基本信息，强制新建表并且储存到数据库中
    参数：volume=[int] 队员数量
    返回：数据库影响行数
    """
    if volume<=0: return 0 #参数无效，返回

    ##从API拿数据
    init_api_client()
    res=get_batch_player(0,volume)
    if fetch_data(res)==0: return 0 #未获取到API数据，返回
    
    ##写入MySQL
    sqlConnection()
    if createTable("player",res,True)==0: return 0 #建表失败，返回
    
    #将API返回结果，转化成参数
    param=api_transfer_sql(res)
    #插入数据
    str=sqlColumn(res)
    sql="insert into player("+str["key"]+") values ("+str["s"]+")"
    row=sqlInsert(sql,param)
    
    #关闭数据库
    sqlDisconnection()
    return row

def sync_item():
    """将API获取到的道具基本信息，强制新建表并且储存到数据库中
    参数：无
    返回：数据库影响行数
    """

    ##从API拿数据
    init_api_client()
    res=get_item()
    if fetch_data(res)==0: return 0 #未获取到API数据，返回
    
    ##写入MySQL
    sqlConnection()
    if createTable("item",res,True)==0: return 0 #建表失败，返回
    
    #将API返回结果，转化成参数
    param=api_transfer_sql(res)
    #插入数据
    str=sqlColumn(res)
    sql="insert into item("+str["key"]+") values ("+str["s"]+")"
    row=sqlInsert(sql,param)
    
    #关闭数据库
    sqlDisconnection()
    return row

def sync_hero():
   
    return 0