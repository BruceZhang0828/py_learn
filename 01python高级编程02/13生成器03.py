def gen():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i+=1


g=gen()
g.__next__()
#g.send()   #send() takes exactly one argument