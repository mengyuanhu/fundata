# -*- coding: utf-8 -*-
import pymysql


##新建mysql连接
def sqlConnection(database="dota"):
    """新建全局的sql连接和游标
    参数：（选填）database默认是dota， 返回：无
    连接使用的用户python，密码python，数据库dota
    """
    global sqlCon
    sqlCon=pymysql.connect(
        host='localhost',
        port=3306,
        user='python',
        password='python',
        db=database,
        charset='utf8'
        )
    global cursor
    cursor=sqlCon.cursor()

##关闭mysql连接和游标
def sqlDisconnection():
    """关闭游标和sql连接
    参数：无， 返回值：无
    """
    cursor.close()
    sqlCon.close()
    
    print("close success")

##select查询
def sqlSelect(query,param):
	"""新建查询
	参数：query是查询sql语句+查询条件
	例如：query="select * from userinfo where name=%s and password=%s", param=[user,pwd]
	返回：游标查询到的数据，tuple格式
	"""

	if len(query)>0 and len(param)>0: #判断是否有查询参数
		try: #尝试启动查询
			row=cursor.execute(query,param)
			if row>0: #查询正确
				res=cursor.fetchall()
				print("success: effect row: "+str(row))
				return res
			else: #查询返回结果有问题
				print("fail: effect row: 0")
				return 0
		except Exception as e: #查询异常
			print("fail: cannot find any data")
			return 0
	else: #查询语句有问题
		print('invalid query')
		return 0
	return 0

##insert插入
def sqlInsert(query,param):
	"""新建插入
	参数：query是插入sql语句+插入数据值（现在是单条）
	例如：query="insert into userinfo (id,name) values (%s,%s)", param=[(1, '123'),(2,'345')] 必须包含[ ]以list格式传入
	注意即便是int也要写%s
	返回：影响行数
	"""

	if len(query)>0 and len(param)>0: #判断是否有插入参数
		try: #尝试启动插入
			row=cursor.executemany(query,param)
			if row>0: #查询正确
				sqlCon.commit() #提交事务
				print("success: effect row: "+str(row))
				return row
			else: #查询返回结果有问题
				print("fail: effect row: 0")
				return 0
		except Exception as e: #查询异常
			sqlCon.rollback() #回滚事务
			print("fail: cannot insert any data")
			return 0
	else: #查询语句有问题
		print('invalid query')
		return 0
	return 0


##表的列名
def columnName(table):
	"""根据表名，在information_schema.columns中查询列名
	参数table是表名，返回值是tuple列名，例如(('id',), ('real_name',), ('name',), ('nation',), ('position',))
	"""
	return sqlSelect("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema=%s AND table_name=%s",["dota",table])