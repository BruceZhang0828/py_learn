'''类就是一组用来描述如何生成一个对象的代码
    class 也是一个对象 动态创建
    type 测一个对象的类型  type也可以来创建一一个类 type('',(){})
'''

class Person(object):
    print('this is person class')

    def __init__(self):
        self.name = 'abc'


def printNum(self):
    print('num is %d'%self.num)
Test2 = type('Test2',(),{'num':0,'printNum':printNum})
t2 = Test2()
print(t2.num)
t2.printNum()