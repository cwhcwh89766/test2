# from views import *
import re
import urls


# 自定义应用处理用户请求
def application(environ,start_response):
    """

    :param environ:用户请求的环境变量，字典
    :param start_response:系统提供生成响应头的函数
    :return: 必须是一个可迭代对象
    """
    path = environ.get("PATH_INFO")
    # print(path)
    # 实现路由：将用户的请求装换为对应函数调用

    for pattern,func in urls:

        # 使用模式匹配请求路径
        res = re.match(pattern,path)
        if res:
            return func(environ,start_response)

    # if path == '/':  # 首页
    #     return index(environ,start_response)
    start_response("200 ok",[('content-type','text/html')])
    return [b'Hello world']