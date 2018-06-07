
class person(object):
    def __init__(self,newName,newAge):
        self.name =newName
        self.age = newAge

laowang = person('老王',20)
print(laowang.age)
print(laowang.name)
laowang.addr = '北京市朝阳区...' #动态添加属性
print(laowang.addr)


