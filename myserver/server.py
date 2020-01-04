# 自定义web服务器

# 可以创建测试服务器
from wsgiref.simple_server import make_server
from application import application



# 创建服务器
sv = make_server('127.0.0.1',9999,application)
print("服务器启动了....9999")
# 开启事件循环，等待用户请求
sv.serve_forever()