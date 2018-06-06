def func_out(pre = 'hello'):#相当于先调这个装饰器  返回值依然是一个装饰器
    print('传递是参数是%s'%pre)
    def func(funName):
        def func_in():
            print('---记录日志---')
            re = funName()
            return re
        return func_in
    return func
@func_out('hahah')#装饰器带参数  =>需要在原来的装饰器外边再定义一个函数
def test():
    print('---test1---')

test()