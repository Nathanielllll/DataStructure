class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newBranch):
        if self.leftChild == None:
            node = BinaryTree(newBranch)
            self.leftChild = node
        else:   # 具有现有左孩子的节点，我们插入一个节点并将现有的子节点放到树中的下一个层。
            node = BinaryTree(newBranch)
            node.leftChild = self.leftChild
            self.leftChild = node

    def insertRight(self, newBranch):
        if self.rightChild == None:
            node = BinaryTree(newBranch)
            self.rightChild = node
        else:   # 具有现有左孩子的节点，我们插入一个节点并将现有的子节点放到树中的下一个层。
            node = BinaryTree(newBranch)
            node.rightChild = self.rightChild
            self.rightChild = node

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end=" ")


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



def buildParseTree(fpexp):
    fplist = fpexp.split()
    # 遍历树的时候，保持跟踪父对象的简单解决方案是用栈
    # 当我们想要返回当前节点的父节点时，我们将父节点从栈中弹出
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == "(":
            # 添加一个新节点作为当前节点的左子节点
            currentTree.insertLeft("")
            pStack.push(currentTree)
            # 并下降到左子节点
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            # 当前符号是数字，将当前节点的根值设为该数字
            currentTree.setRootVal(i)
            # 返回父节点
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            # 当前符号是运算符，将当前节点的根值设为该运算符
            currentTree.setRootVal(i)
            # 添加一个新节点作为当前节点的右子节点
            currentTree.insertRight("")
            pStack.push(currentTree)
            # 下降到右子节点
            currentTree = currentTree.getRightChild()
        elif i == ')':
            # 返回父节点
            parent = pStack.pop()
            currentTree = parent
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( 3 + ( 4 * 5 ) )")
postorder(pt)



def evaluate(parseTree):
    import operator
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(int(evaluate(leftC)), int(evaluate(rightC)))
    else:
        return parseTree.getRootVal()

print(evaluate(pt))




















