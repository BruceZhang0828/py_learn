class Person(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'asd'
    #属性访问时 拦截器 , 打log
    def __getattribute__(self, item):
        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self,item)


a = Person('python')
print(a.subject1)
print(a.subject2)