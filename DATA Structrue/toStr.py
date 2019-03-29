"""整数转换为任意进制字符串"""

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

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

rStack = Stack()
def toStr_2(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n=n//base

    res = ""
    while not rStack.is_empty():
        res = res+str(rStack.pop())
    return res

print(toStr(10,2))
print(toStr_2(10,2))




