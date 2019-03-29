"""后缀表达式求值"""

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

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixEval(postfixExpr):
    operandStack = stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

print(postfixEval('7 8 + 3 2 + /'))











