# -*- coding: utf-8 -*-
from sync.syncTrans import sync_match
from fundata.dota2.player.player_info import get_batch_player
from fundata.client import init_api_client
from mysql.sqlConnect import sqlConnection,sqlDisconnection,sqlInsert,createTable
from mysql.dataHandler import api_transfer_sql,sqlColumn
def testApiSql():
    ##从API拿数据
    init_api_client()
    res_a=get_batch_player(0,5)
    
    ##写入MySQL
    cur=sqlConnection()
    
    #建表
    createTable("player_test",res_a,True)
    
    #将API返回结果，转化成参数
    param=api_transfer_sql(res_a)
    #插入数据
    str=sqlColumn(res_a)
    sql="insert into player_test("+str["key"]+") values ("+str["s"]+")"
    print (sql)
    row=sqlInsert(sql,param)
    print("插入数据")
    print(row)
    
    #关闭数据库
    sqlDisconnection()

if __name__ == "__main__":

   testApiSql()
  

   







    
