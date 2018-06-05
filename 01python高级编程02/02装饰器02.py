'''装饰器:把函数打扮的漂漂亮亮的
    开放封闭原则
    语法糖:@,特殊功能
'''
def test1():
    print('---1---')

def test1():
    print("---2---")

#test1()

def w1(func):
    def inner():
        if True:
            print('---正在检查---')
            func()
        else:
            return None
    return inner
@w1#这个就是装饰器
def f1():
    print('---f1---')
@w1
def f2():
    print('---f2---')

#innerFunc = w1(f1)
#innerFunc()
#f1()

def makeblood(fn):
    def wrapped():
        return '<b>'+fn()+'</b>'

    return wrapped

def makeItalic(fn):
    def wrapped():
        return '<r>'+fn()+'</r>'

    return wrapped

@makeblood
def test3():
    return 'helloworld-3'
@makeItalic
def test4():
    return 'helloworld-4'

@makeblood#先装饰这个但是执行的时候 执行下边的装饰
@makeItalic#第一个装饰执行的是 第二装饰内容
def test5():
    return 'helloworld-5'

#装饰器什么时候进行装饰 @w 装饰器已经开始执行了 而不是下边函数调用的时候的开始的

#print(test3())
#print(test4())
print(test5())