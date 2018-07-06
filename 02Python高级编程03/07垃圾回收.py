#垃圾回收
import gc

class ClassA(object):
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))

def f():
    print('---0---')
    a1 = ClassA()
    a2 = ClassA()
    a1.t = a2
    a2.t = a1
    print('---1---')
    del a1
    del a2
    print('---2----')
    print(gc.garbage)
    print('---3----')
    print(gc.collect())#显示执行垃圾回收
    print('---4----')
    print(gc.garbage)
    print('---5---')
'''
垃圾回收后的对象会放在gc.garbage列表⾥⾯
gc.collect()会返回不可达的对象数⽬，4等于两个对象以及它们对应的dict
'''
if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK)
    f()
