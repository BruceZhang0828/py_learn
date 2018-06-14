class Person(object):
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
# __shots__ 变量 来限制该class实例能添加的属性

p = Person('老王',10)
p.addr = '北京' #  'Person' object has no attribute 'addr'
