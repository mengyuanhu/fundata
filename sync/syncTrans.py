#调用别的文件夹中py时使用
import os
import sys
current_dir = os.getcwd()    # obtain work dir
sys.path.append(current_dir) # add work dir to sys pat

import time
from fundata.client import init_api_client
from fundata.dota2.match import get_batch_basic_info
from mysql.sqlConnect import sqlConnection,sqlDisconnection,sqlInsert
from mysql.dataHandler import api_transfer_sql, sqlColumn

def sync_match(s_time,volume):
    """从api多次读取match信息，并且插入mysql数据库
    参数：s_time是str，例如"2020-1-1 00:00:00"；limit是int，需要数据条数
    返回：影响行数，未写完
    """
    if volume<=0: return 0
    #转化时间为时间戳，设置初始值
    start_time=int(time.mktime(time.strptime(s_time, "%Y-%m-%d %H:%M:%S")))
    start_from=0
    limit=200 #API接口请求的最大限额
    
    #初始化api和mysql，
    init_api_client()
    cur=sqlConnection()


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