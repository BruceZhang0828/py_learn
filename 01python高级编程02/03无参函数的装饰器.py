def func(funcName):
    print('---func1---')
    def func_in(*argc,**kwargs):
        print('---func_in1---')
        funcName(*argc,**kwargs)
        print('---func_in2---')
    return func_in

@func
def test(a,b,c):
    print(a+b+c)

#test = func(test)
test(10,25,10)