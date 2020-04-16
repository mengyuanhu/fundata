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

def sync_match_backup(s_time,s_from,volume):
    """从api多次读取match信息，并且插入mysql数据库。
    -当轮询API请求中断时，重试3次
    
    参数：s_time=[str]，例如"2020-1-1 00:00:00"；
    s_from=[int]，默认是0，如果是继续取值，则写match_id
    volume=[int]，需要数据条数
    
    返回：dict={
    "apiSuc":[int], #完成1，未完成0，已经没有更多数据2
    "sqlSuc":[int], #完成1，未完成0
    "row":[int], #影响行数
    "match_id":[int]} #最后一次请求使用的match_id
    """
    dict={"apiSuc":1,"sqlSuc":1,"row":0,"match_id":0}

    if volume<=0: #传参为0，api完成并返回
        dict["apiSuc"]=1
        dict["apiSuc"]=0
        return dict

    #转化时间为时间戳，设置初始值
    start_time=int(time.mktime(time.strptime(s_time, "%Y-%m-%d %H:%M:%S")))
    if s_from>0: start_from=s_from
    else:start_from=0
    limit=200 #API接口请求的最大限额
    retry=3 #重试次数的上限
    
    #初始化api和mysql
    init_api_client()
    sqlConnection()


    #新建插入Sql语句变量
    param=[]
    sql=[]

    #进入循环：当获取数据条数总数，大于api上限时，分批请求
    while volume//limit>0: 
        res=get_batch_basic_info(start_time,start_from,limit)
        if fetch_data(res)==0:  #本次获取API数据失败,记录match_id, 跳出循环
            dict["apiSuc"]=0
            dict["match_id"]=start_from
            break
        param=param+api_transfer_sql(res) #将api的返回值转化为mysql需要的参数，并且拼接起来
        print("start from matchID=%s, volume remain=%s, param lenth=%i"%( start_from,volume,len(param)))
        
        if len(res["data"])<limit:  #当API返回数据条目数<limit，说明没有更多数据了，跳出循环
            dict["apiSuc"]=2
            break
        
        #组成下一次API请求的参数，接着请求
        volume=volume-limit
        start_from=res["data"][len(res["data"])-1]["match_id"] #获取最后一个match_id

    
    else: #总数（剩余总数）<上限，并且不是被上限整除，最后一次请求
        if volume>0:
            res=get_batch_basic_info(start_time,start_from,volume)#···API多返回一条，不知道为什么
            if fetch_data(res)==0:  #本次获取API数据失败,记录match_id
                dict["apiSuc"]=0
                dict["match_id"]=start_from
            param=param+api_transfer_sql(res) 
            print("Finally: start from matchID=%s, volume remain=%s, param lenth=%i"%(start_from,volume,len(param)))
        
    #完成循环：如果API取数正常，保留最后一次match_id
    if dict["apiSuc"]==1: 
        dict["match_id"]=res["data"][len(res["data"])-1]["match_id"]
    else:#多获取一条数据，以免之前fail时res无数据
        res=get_batch_basic_info(start_time,0,1) 

    #创建表，生成插入sql语句
    if createTable("match_basic",res)==0:
        dict["sqlSuc"]=0
        dict["match_id"]=0 #建表失败，数据都无法储存，需要重新获取API数据
        return dict #建表失败，返回
    str_a=sqlColumn(res)
    sql="insert into match_basic("+str_a["key"]+") values ("+str_a["s"]+")" #生成插入sql语句

    #执行插入
    dict["row"]=sqlInsert(sql,param)
    dict["sqlSuc"]=1
    #关闭数据库
    sqlDisconnection()
    return dict

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