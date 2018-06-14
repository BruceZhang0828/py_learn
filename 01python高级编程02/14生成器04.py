def test1():
    while True:
        print('------1------')
        yield None

def test2():
    while True:
        print('-------2-------')
        yield None

t1 = test1()
t2 = test2()


#相当于同时执行两个while , 多任务的一种实现方式--协程 (协程 进程 线程)
while True:
    t1.__next__()
    t2.__next__()