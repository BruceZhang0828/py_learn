class Test(object):
    def __init__(self,func):
        print('-----初始化------')
        print('func name is %s'%func.__name__)
        self.__func = func
    def __call__(self, *args, **kwargs):
        print('------装饰器中的功能-------')
        self.__func()


#t = Test();
#t() 调用__call__方法
#__new__ __init__
@Test #这里执行了 __init__方法
def test():
    print('-------test-------')

test()# test = Test(test) 类装饰器的作用
test()