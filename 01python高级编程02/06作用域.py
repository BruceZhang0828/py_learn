#命名空间:起作用的范围
#全局变量:
#局部变量:局部变量 > 全局变量 legb原则 局部=>闭包=>全局=>python给的
def test():
    print('---test---')
    a = 100
    b = 100

print(locals())