
def api_transfer_sql(res):
    """将fundata api获取的数据，处理成mysql插入需要的传入值
    参数dict格式，例如{'retcode': 200, 'data': [{'id': 106863163, 'real_name': 'Lu Yao 路垚', 'name': 'SoMnus丶M', 'nation': 'CN', 'position': 2}, {'id': 101695162, 'real_name': 'Xu Linsen 徐林森', 'name': 'FY', 'nation': 'CN', 'position': 4}]}
    返回list格式，例如[(106863163, 'Lu Yao 路垚', 'SoMnus丶M', 'CN', 2), (101695162, 'Xu Linsen 徐林森', 'FY', 'CN', 4)]
    """
    #检查返回状态码
    res_list=fetch_data(res)
    if res_list!=0:
            param=[]
            #遍历查找所有的值
            for i, t_dict in enumerate(res_list): #第一轮循环遍历，查询到(1,'x')
                t_list=[]
                for key, value in t_dict.items(): #第二轮循环遍历，获得值'x'
                    t_list.append(value)
                param.append(tuple(t_list)) #
                i=i+1
            return param
    else:
        return 0

def sqlColumn(res):
    """生成Insert语句中的列名
    参数：API返回数据
    返回：用于SQL String的字典格式数据，例如 
    dict={"key":"id, real_name, name, nation, position",
    "s":"%s,%s,%s,%s,%s"}
    """
    #检查返回状态码
    res_list=fetch_data(res)

    if res_list!=0:
        str_key=""
        str_s=""
        for key, value in res["data"][0].items():#遍历第[0]号数据的每一个键
            str_key+="%s,"%(key)
            str_s+="%s,"
        return {"key":str_key[:-1],"s":str_s[:-1]}#返回时，去掉最后一个逗号
    else: return {"key":"","s":""}#没有数据，按照约定格式返回空


def fetch_data(res):
    """检查返回状态码，如果正确，返回data部分，否则打印报错原因并且返回0
    参数：API返回数据
    """
    if res["retcode"] ==10000:
        print("parameters error，出现了传参错误")
        return 0
    elif res["retcode"] ==10001:
        print("data not found，没有找到对应的数据")
        return 0
    elif res["retcode"]==10002:
        print("internal error，出现了内部异常")
        return 0
    elif res["retcode"]==200:
        print("success，即响应成功")
        return (res["data"]) #执行转化
    else:
        print("未知返回值")
        return 0


def get_last_match_id(res_list):
    """未被调用
    """
    return res_list[len(res["data"])-1]["match_id"]