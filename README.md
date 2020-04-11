# fundata
get dota2 info and analyze in mysql

# fundata-python-sdk

api.varena.com Python SDK

## 说明
- SDK 支持的 Python 版本:
    - python2.7
    - python3 (由[codeway3](https://github.com/codeway3)提供支持)
- 文档地址: http://open.varena.com/


## 使用

- 初始化 client
    ```python
    from fundata.client import init_api_client
    
    init_api_client('public_key', 'secert_key')
    ```

    初始化时，需要设置 `public_key` `secert_key`，可以在 **http://open.varena.com/** 上申请 API key，通过后，会收到邮件回复获取到对应的 key

- 调用某个接口
    ```python
    from fundata.client import get_api_client

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/basic-info'
    data = {"match_id": 3765833999}
    res = client.api(uri, data)

    # 增加对 res 的处理
    # 请求失败时，res 返回的是 False
    # 如果是解析响应失败，则会返回 {"retcode": -1, message:"xxx" } 的数据
    # 正常的响应一般是 { "retcode": 200, "message": "", "data": {} } }
    # 一般是先判断 res 是不是 False，然后判断返回对象的 recode 是否为 200
    ```

## 实现的 API 调用
- dota2
    - match
        - single
        - batch 
            - [x] `/data-service/dota2/public/batch/match/basic_info` -> fundata.dota2.match.batch.get_batch_basic_info



##开发环境搭建
    1. 安装VS 2019 Community
    2. 安装Python（勾选pip选项）
	    2.1. 配置环境变量，新增Python 安装路径
	    2.2. 在Python安装路径，运行shell脚本，用pip install命令安装requests, ipython, jupyter, pymysql, mysql（不确认是否一定安装）
    3.配置Jupyter
	    3.1. 先运行 jupyter notebook --generate-config，生成配置文件
	    3.2. 在配置文件 C:\Users\<user_name>\.jupyter\jupyter_notebook_config.py中，找到c.NotebookApp.notebook_dir增加目录，并去掉#，保存。
	    3.3. 运行jupter notebook，启动网页编辑
	    #3.4. 运行jupyter notebook password，新增密码tyyhu1026
    4. 安装MySQL
	    4.1. 下载 mysql-8.0.19-winx64
	    4.2. 安装和初始化
	    4.3. 在date下，找到.err 结尾的文件找到初始密码 A temporary password is generated for root@localhost: 4mlkwV>sfaU+
    5. 安装Navicat并激活，连接数据库，修改新密码dota2
    6. 设置固定IP
    7. 添加新用户manu密码dota2，修改成可远程访问的用户（修改mysql-user表中Host为%）
    8. 添加新用户python密码python，用来给python连接数据库
    9. 在Github注册账户mengyuanhumy@163.com,密码tyyHU1026，新建仓库fundata
    10. 在VS安装扩展github，登录Github的用户，并且同步代码。