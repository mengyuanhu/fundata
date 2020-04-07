
def api_transfer_sql(res):
    """将fundata api获取的数据，处理成mysql插入需要的传入值
    参数dict格式，例如{'retcode': 200, 'data': [{'id': 106863163, 'real_name': 'Lu Yao 路垚', 'name': 'SoMnus丶M', 'nation': 'CN', 'position': 2}, {'id': 101695162, 'real_name': 'Xu Linsen 徐林森', 'name': 'FY', 'nation': 'CN', 'position': 4}]}
    返回list格式，例如[(106863163, 'Lu Yao 路垚', 'SoMnus丶M', 'CN', 2), (101695162, 'Xu Linsen 徐林森', 'FY', 'CN', 4)]
    """

    #检查返回状态码
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
        return trans(res["data"]) #执行转化
    else:
        print("未知返回值")
        return 0


def trans(res_list):
    """将返回值的data部分，取出数值部分，放入list中，直接用户mysql插入
    参数：res中data部分，例如[(1,'x'),(2,'y'),(3,'z')]
    返回：list
    """
    param=[]
    for i, t_dict in enumerate(res_list): #第一轮循环遍历，查询到(1,'x')
        t_list=[]
        for key, value in t_dict.items(): #第二轮循环遍历，获得值'x'
            t_list.append(value)
        param.append(tuple(t_list)) #
        i=i+1
    return param

def get_last_match_id(res_list):
    """
    """
    return res_list[len(res["data"])-1]["match_id"]