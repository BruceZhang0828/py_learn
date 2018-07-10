class Person():
    def __getattribute__(self, item):
        print('执行属性拦截')
        if(item.startswith('a')):
            return 'hahaha'
        else:
            return self.test



    def test(self):
        print('heihei...')


p = Person()
p.a

p.b#产生了递归调用...导致程序出错.