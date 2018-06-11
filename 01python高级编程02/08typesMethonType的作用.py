import types
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def eat(self):
    print('---一直吃----')

p1 =Person('p1',1)

p1.eat = types.MethodType(eat,p1)

p1.eat()

xxx = types.MethodType(eat,p1)
xxx()

@staticmethod
def func1():
    print('===static methon===')

@classmethod
def func2(cls):
    print('===class methond===')

Person.func1 = func1
Person.func2 = func2
Person.func1()
Person.func2()


