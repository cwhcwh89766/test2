# 视图处理函数
import os


def index(environ,start_response):
    start_response("200 ok",[("content-type","text/html")])
    html = """
    <html>
    <head><meta charset='utf-8'></head>
    <body>
        <h1>欢迎访问我的站点</h1>
    </body>
    </html>
    """
    return [html.encode('utf8')]


def login(environ,start_response):
    start_response("200 ok",[("content-type","text/html")])
    html = """
    <html>
    <head><meta charset='utf-8'></head>
    <body>
        <h1>html</h1>
    </body>
    </html>
    """
    return [html.encode('utf8')]


def load_html(environ,start_response,*args):
    file_name = args[-1]
    print(file_name)

    start_response("200 ok",[("content-type","text/html")])
    path = 'templates/' + file_name  # 拼接文件路径
    if os.path.exists(path):
        with open(path,'rb') as fp:
            # 读取文件内容
            html = fp.read()
    else:
        html = "你请求的页面不存在".encode('utf8')
    return [html]


def load_picture(environ,start_response,*args):
    file_name = args[-2]
    print(file_name)
    ext = os.path.splitext(file_name)
    start_response("200 ok",[("content-type","image/")])
    path = 'templates/images/' + file_name  # 拼接文件路径
    if os.path.exists(path):
        with open(path,'rb') as fp:
            # 读取文件内容
            html = fp.read()
    else:
        html = "你请求的页面不存在".encode('utf8')
    return [html]