# fundata
get dota2 info and analyze in mysql

# fundata-python-sdk

api.varena.com Python SDK

## ˵��
- SDK ֧�ֵ� Python �汾:
    - python2.7
    - python3 (��[codeway3](https://github.com/codeway3)�ṩ֧��)
- �ĵ���ַ: http://open.varena.com/


## ʹ��

- ��ʼ�� client
    ```python
    from fundata.client import init_api_client
    
    init_api_client('public_key', 'secert_key')
    ```

    ��ʼ��ʱ����Ҫ���� `public_key` `secert_key`�������� **http://open.varena.com/** ������ API key��ͨ���󣬻��յ��ʼ��ظ���ȡ����Ӧ�� key

- ����ĳ���ӿ�
    ```python
    from fundata.client import get_api_client

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/basic-info'
    data = {"match_id": 3765833999}
    res = client.api(uri, data)

    # ���Ӷ� res �Ĵ���
    # ����ʧ��ʱ��res ���ص��� False
    # ����ǽ�����Ӧʧ�ܣ���᷵�� {"retcode": -1, message:"xxx" } ������
    # ��������Ӧһ���� { "retcode": 200, "message": "", "data": {} } }
    # һ�������ж� res �ǲ��� False��Ȼ���жϷ��ض���� recode �Ƿ�Ϊ 200
    ```

## ʵ�ֵ� API ����
- dota2
    - match
        - single
        - batch 
            - [x] `/data-service/dota2/public/batch/match/basic_info` -> fundata.dota2.match.batch.get_batch_basic_info



##���������
    1. ��װVS 2019 Community
    2. ��װPython����ѡpipѡ�
	    2.1. ���û�������������Python ��װ·��
	    2.2. ��Python��װ·��������shell�ű�����pip install���װrequests, ipython, jupyter, pymysql, mysql����ȷ���Ƿ�һ����װ��
    3.����Jupyter
	    3.1. ������ jupyter notebook --generate-config�����������ļ�
	    3.2. �������ļ� C:\Users\<user_name>\.jupyter\jupyter_notebook_config.py�У��ҵ�c.NotebookApp.notebook_dir����Ŀ¼����ȥ��#�����档
	    3.3. ����jupter notebook��������ҳ�༭
	    #3.4. ����jupyter notebook password����������tyyhu1026
    4. ��װMySQL
	    4.1. ���� mysql-8.0.19-winx64
	    4.2. ��װ�ͳ�ʼ��
	    4.3. ��date�£��ҵ�.err ��β���ļ��ҵ���ʼ���� A temporary password is generated for root@localhost: 4mlkwV>sfaU+
    5. ��װNavicat������������ݿ⣬�޸�������dota2
    6. ���ù̶�IP
    7. ������û�manu����dota2���޸ĳɿ�Զ�̷��ʵ��û����޸�mysql-user����HostΪ%��
    8. ������û�python����python��������python�������ݿ�
    9. ��Githubע���˻�mengyuanhumy@163.com,����tyyHU1026���½��ֿ�fundata
    10. ��VS��װ��չgithub����¼Github���û�������ͬ�����롣