# print('\033[30m打印前景色0\033[0m')
# print('\033[31m打印前景色1\033[0m')
# print('\033[32m打印前景色2\033[0m')
# print('\033[33m打印前景色3\033[0m')
# print('\033[34m打印前景色4\033[0m')
# print('\033[35m打印前景色5\033[0m')
# print('\033[36m打印前景色6\033[0m')
# print('\033[37m打印前景色7\033[0m')
# print('\033[40m打印背景色0\033[0m')
# print('\033[41m打印背景色1\033[0m')
# print('\033[42m打印背景色2\033[0m')
# print('\033[43m打印背景色3\033[0m')
# print('\033[44m打印背景色4\033[0m')
# print('\033[45m打印背景色5\033[0m')
# print('\033[46m打印背景色6\033[0m')
# print('\033[47m打印背景色7\033[0m')
# print('\033[0m打印显示方式0\033[0m')
# print('\033[1m打印显示方式1\033[0m')
# print('\033[4m打印显示方式4\033[0m')
# print('\033[5m打印显示方式5\033[0m')
# print('\033[7m打印显示方式7\033[0m')
# print('\033[8m打印显示方式8\033[0m')
# print('\033[5;31;47m综合打印\033[0m')

# from colorama import Fore,Back,Style,init
#
# init(autoreset=True)
# print(Fore.RED + '打印红色文字')
# print(Back.GREEN + '设置背景为绿色')
# print('恢复默认')


from PIL import Image # PIL 是一个 Python 图像处理库

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的

WIDTH = 60 # 字符画的宽
HEIGHT = 45 # 字符画的高


# 将256灰度映射到70个字符上，也就是RGB值转字符的函数：
def get_char(r, g, b, alpha=256):  # alpha透明度
   if alpha == 0:
       return ' '
   length = len(ascii_char)
   gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
   unit = (256.0 + 1) / length
   return ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符
   # 通过灰度来区分色块


if __name__ == '__main__':
   img = '../images/22.jpg' # 图片所在位置
   im = Image.open(img)
   im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
   txt = ""
   for i in range(HEIGHT):
       for j in range(WIDTH):
           txt += get_char(*im.getpixel((j, i))) # 获得相应的字符
       txt += '\n'
   print(txt)  # 打印出字符画
   # 将字符画 写入文件中
   with open("../images/0.txt", 'w') as f:
       f.write(txt)