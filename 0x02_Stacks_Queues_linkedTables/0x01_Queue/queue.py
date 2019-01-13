#coding=utf-8
class Node(object):#先获取到节点，节点有两个作用，1.进行一个指针（假设的）一个指向，
                    # 2,。就是现在这个位置上的元素的值
    def __init__(self,val):
        self.next=None  #指针的下一个，用于指向内容，先给初始化设置为空
        self.val=val   #val是它原本的值，

class Queue(object):
    def __init__(self): #初始化两个属性，分别代表first头和last
        self.first=None
        self.last=None
    def enter(self,n):  #开始进队列
        #实例节点
        n = Node(n)  # 指定在第5个位置上
        #进队列时需要先判断队列是不是空，如何判断，通过判断first是不是空
        if self.first==None:
            self.first=n  #为什么为空了还要把值赋值给first
            self.last=self.first
        else:#进队列，first不变，last的位置向后移动一个
            self.last.next=n   #指针指向后面一个  #把下移后的指向给lst.netx
            self.last=n   #赋值值给last

    def quit(self): #退出队列，
        #退出队列就是
        if self.first==None:
            return None
        else:
            tmp=self.first.val   #获取项目的值
            self.first=self.first.next
        return tmp
    def allQuit(self):#全部退出
        Lists=[] #用户保存数据
        while self.first!=None:
            Lists.append(self.first.val)  #把每一次的值存入到一个list中
            self.first=self.first.next
        return Lists

if __name__=="__main__":
    q=Queue()
    q.enter(1)
    q.enter(2)
    q.enter(3)

    print(q.quit())
    print(q.quit())
    print(q.quit())

    # print q.allQuit()