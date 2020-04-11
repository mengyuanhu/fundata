import webbrowser

def api_generate_table(res_list):
    """将API返回值的data部分，取出列名和列值
    参数：res中data部分，例如[(1,'x'),(2,'y'),(3,'z')]
    返回：HTML Table
    """
    str='<table border="1">'
    #生成列名
    str+='<tr>'
    for key, value in res_list[0].items():
        str+='<th>%s</th>'%(key)
    str+='</tr>'
    
    #生成列值
    for i, t_dict in enumerate(res_list): #第一轮循环遍历，查询到(1,'x')
        str+='<tr>'
        for key, value in t_dict.items(): #第二轮循环遍历，获得值'x'
            str+='<td>%s</td>'% (value)
        str+='</tr>'
        i=i+1
        
    str+='</table>'
    return str

def sql_generate_table(res_list):
    """将MySql返回值的data部分，取出列名和列值
    参数：
    返回：HTML Table
    """
    str='<table border="1">'       
    str+='</table>'
    return str

def generate_web_page(page_name, res, type):
    """将API或者MySql取出的数据生成HMTL页面，并且打开web页面
    参数：page_name网页名称, str，例如test.html
    res数据，即从api或者mysql直接返回的结果
    type类型，只有api和sql两种选择
    """

    #命名生成的html
    GEN_HTML=page_name
    #打开文件，准备写入
    f=open(GEN_HTML,'w')
    
    #页面开头
    str="""
    <html>
    <head>英雄信息</head>
    <body>
    """

    #根据type，打印表格
    if type=='api':
        str+=api_generate_table(res["data"])
    elif type=='sql':
        str+=sql_generate_table(res["data"])
    else:
        str+="<p>wrong type! cannot print any data</p>"


    #展示数据行数
    str+="<p>count=%s</p>"%len(res["data"])
    str+="""
    </body>
    </html>
    """
    #写入文件
    f.write(str) 
    #关闭文件
    f.close()

    #运行完自动在网页中显示
    webbrowser.open(GEN_HTML,new = 1)






 

