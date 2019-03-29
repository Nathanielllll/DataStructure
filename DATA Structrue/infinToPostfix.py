class stack(object):
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


def infixToPostfix(infixexpr):
    """中缀表达式转为后缀表达式"""
    # 当我们看到左括号时，我们保存它，
    # 表示高优先级的另一个运算符将出现。
    # 该操作符需要等到相应的右括号出现以表示其位置（回忆完全括号的算法）。
    # 当右括号出现时，可以从栈中弹出操作符。
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = stack()   # 空栈以保存运算符
    postfixList = []    # 输出列表
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            # 删除已经在 opstack 中具有更高或相等优先级的任何运算符，
            # 并将它们加到输出列表中
            while not opStack.is_empty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)

print(infixToPostfix("( A + B ) * ( C + D )"))





















