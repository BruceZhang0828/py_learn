'''装饰器:把函数打扮的漂漂亮亮的
    开放封闭原则
    语法糖:@,特殊功能
'''
def test1():
    print('---1---')

def test1():
    print("---2---")

test1()

def w1(func):
    def inner():
        print('---正在检查---')
        func()
    return inner
def f1():
    print('---f1---')

def f2():
    print('---f2---')

#innerFunc = w1(f1)
#innerFunc()