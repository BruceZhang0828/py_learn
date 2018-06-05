def func(funcName):
    print('---func1---')
    def func_in(*argc,**kwargs):
        print('---func_in1---')
        return funcName(*argc,**kwargs) #函数的返回值
        #print('---func_in2---')
    return func_in #返回到外边

@func
def test(a,b,c):
    print(a+b+c)
    return a+b+c

#test = func(test)
print(test(10,25,10))