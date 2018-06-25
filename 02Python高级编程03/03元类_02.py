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
'''元类 就是 类的类(元类创建的元类)
   type(...)元类 (创建) => class 
   尽量 不要用type
'''
print(cat.__class__)
print(dog.__class__)
print(Cat.__class__)
print(Dog.__class__)

#__metaclass__属性 定义类的时候定义__metaclass属性的时候
# 定义class的时候 会按照metaclass的内容进行定义
                #foo               object           {'bar':'bip'}
def upper_attr(future_class_name,future_class_parents,future_class_attr,):
    #遍历属性字典,把不是__属性名变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
    #调用 type 来 创建一个类
    return type(future_class_name,future_class_parents,newAttr)

class Foo(object, metaclass = upper_attr):#python3中特别的
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print(f.BAR)

