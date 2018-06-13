def creatNum():
    print('----start----')
    a,b = 0,1
    for i in range(5):
        print('--------1-------')
        yield b
        print('--------2--------')
        a,b = b,a+b
        print('---------3--------')
    print('-------stop-------')
def gen():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i+=1
e = creatNum()
ref = e.__next__() #相当月next(e)
print(ref)
for num in e:
    print(num)



f = gen()
g = f.__next__()
print(g)
f.send('hahah') #相当于 将hahah 赋值于 temp中
h = f.__next__()
print(h)
