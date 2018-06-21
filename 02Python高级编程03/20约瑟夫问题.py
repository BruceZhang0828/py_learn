'''

 约瑟夫环问题：
    已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
    从编号为k的人开始报数，数到k的那个人被杀掉；他的下一个人又从1开始报数，
    数到k的那个人又被杀掉；依此规律重复下去，直到圆桌周围的人只剩最后一个
 思路:当k是1的时候，存活的是最后一个人，
      当k>=2的时候，构造一个n个元素的循环链表，然后依次杀掉第k个人，留下的最后一个是可以存活的人。
'''

class Node(object):
    def __init__(self,value,next =None):
        self.value = value
        self.next = next

def creatLink(n):

    if n<=0:
        return False
    if n==1:
        return Node(1)
    else:
        root = Node(1)
        tmp = root
        for i in range(2,n+1):
            tmp.next = Node(1)
            tmp = tmp.next
        tmp.next = root
        return root
def showLink(root):
    tmp = root
    while True:
        print(tmp.value)
        tmp = tmp.next
        if tmp== None or tmp==root:
            break

def josephus(n,k):
    if k ==1:
        print('survive:%d'%n)
        return
    root = creatLink(n)
    tmp = root
    while True:
        for i in range(k-2):
            tmp = tmp.next
        print('kill:%s'%str(tmp.next.value))
        tmp.next = tmp.next.next
        tmp = tmp.next
        if tmp.next == tmp:
            break
        print('survive:', tmp.value)
if __name__=='__main__':
    josephus(10,4)
    print('-----------------')
    josephus(10,2)
    print('-----------------')
    josephus(10,1)
    print('-----------------')