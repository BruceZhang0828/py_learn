class Person(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'asd'
    #属性访问时 拦截器 , 打log
    def __getattribute__(self, item):
        print('===>1%s'%item)
        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            obj = object.__getattribute__(self, item)
            print('===>2%s' % str(item))
            return obj

    def show(self):
        print('this is itcast')


a = Person('python')
print(a.subject1)
print(a.subject2)
a.show()
#1.show属性 指向一个函数
#2.在执行方法