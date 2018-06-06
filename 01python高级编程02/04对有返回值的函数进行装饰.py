def func(funcName):# 这也是一种通用的模拟器
    print('---func1---')
    def func_in(*argc,**kwargs):
        print('---func_in1---')
        num = funcName(*argc,**kwargs) #函数的返回值
        print('---func_in2---')
        return num
    return func_in #返回到外边

@func
def test(a,b,c):
    print(a+b+c)
    return a+b+c
@func
def test2():
    print('---test2----')
#test = func(test)
print(test(10,25,10))
test2()