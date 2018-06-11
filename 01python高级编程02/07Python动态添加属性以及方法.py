import  types
class person(object):
    def __init__(self,newName,newAge):
        self.name =newName
        self.age = newAge

laowang = person('老王',20)
print(laowang.age)
print(laowang.name)
laowang.addr = '北京市朝阳区...' #动态添加属性
print(laowang.addr)
person.num = 100
print(laowang.num)
'''动态添加方法:
    
'''

def run(self):
    print('----%s正在跑----'%self.name)

laowang.run = run

laowang.run(laowang)# run属性指向函数 但是还需要进行传递参数
                    # laowamg.run()还没有把laowang当参数传递到run函数中
yanglei = person('yanglei',20)

yanglei.run = types.MethodType(run,yanglei)
yanglei.run()


