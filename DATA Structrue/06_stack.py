class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新元素item到栈顶"""
        self.__list.append(item)  ## 对顺序表尾部，为O(1), 头部为O(n)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

