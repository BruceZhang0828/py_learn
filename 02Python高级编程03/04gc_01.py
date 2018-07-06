'''小整数 对象池  [-5,257) 不会被垃圾回收
   大整数 每一次都是创建新的对象
   单个字符共用对象, 常驻内存
    单个单词 不可修改 默认开启intern机制 共用对象 引用计数为0 则销毁
'''


a = 'hello world'
b ='hello world'
print(id(a))
print(id(b))
c = 1356
d = 1356
print(id(c))
print(id(d))