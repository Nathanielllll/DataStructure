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

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())








