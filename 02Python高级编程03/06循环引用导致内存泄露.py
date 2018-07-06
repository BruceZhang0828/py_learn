import gc
class A():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f():
    while True:
        a1=A()
        a2=A()
        a1.t = a2
        a2.t = a1
        del a1
        del a2

gc.disable()
f()
'''
创建了a1，a2后这两块内存的引⽤计数都是1，执
⾏ a1.t=a2 和 a2.t=a1 后，这两块内存的引⽤计数变成2.
在del a1后，内存1的对象的引⽤计数变为1，由于不是为0，所以内存1
的对象不会被销毁，所以内存2的对象的引⽤数依然是2，在del a2后，
同理，内存1的对象，内存2的对象的引⽤数都是1。
虽然它们两个的对象都是可以被销毁的，但是由于循环引⽤，导致垃圾
回收器都不会回收它们，所以就会导致内存泄露
'''