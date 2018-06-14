#生成器
#一边循环一边计算的机制 称为生成器

a = [x*2 for x in range(10)]
b = (x*2 for x in range(10)) #生成器 如果调用到最后一个 继续调用 抛出异常

print(a)
print(next(b))

#斐波拉契数列
def ceateNum():
    print('-------start------')
    c,d = 0,1
    for i in range(5):
        yield d #只要加上yield 就成了生成器
        c,d = d,c+d
    print('-------end------')
e = ceateNum()
print(next(e))
print(next(e))
#print(e)