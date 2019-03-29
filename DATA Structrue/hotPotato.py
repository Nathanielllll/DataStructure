class Queue(object):

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """添加一个新元素item到队列"""
        self.__list.append(item)  ## 对顺序表尾部，为O(1) ## 总有O(1)和O(n)，看哪个执行的次数多

    def dequeue(self):
        """列表头部删除一个元素"""
        return self.__list.pop(0)  ## 从头部删除，复杂度为0(n)

    def is_empty(self):
        """判断列表是否为空"""
        return self.__list == []

    def size(self):
        return len(self.__list)



def hotPotato(namelist, num):
    """烫山芋问题"""
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))










