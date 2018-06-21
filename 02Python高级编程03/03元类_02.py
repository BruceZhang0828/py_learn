class Animal(object):
    def eat(self):
        print('--------eat--------')

class Dog(Animal):
   pass


Cat = type('Cat',(Animal,),{})#type创建对象之 继承关系

cat = Cat()
cat.eat()
dog = Dog()
dog.eat()
'''元类 就是 类的类
   type(...)元类 (创建) => class 
   尽量 不要用type
'''
print(Cat.__class__)
print(Dog.__class__)