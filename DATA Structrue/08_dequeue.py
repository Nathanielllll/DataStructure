


class Dequeue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """添加一个新元素item到队列"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        """列表头部删除一个元素"""
        return self.__list.pop(0)  ## 从头部删除，复杂度为O(n)

    def pop_rear(self):
        return self.__list.pop()  ## 从尾部删除，复杂度为O(1)

    def is_empty(self):
        """判断列表是否为空"""
        return self.__list == []

    def size(self):
        return len(self.__list)