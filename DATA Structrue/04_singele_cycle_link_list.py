class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0

        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return

        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem, end=' ')
        print("")

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node

        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self._head
            self._head = node
            cur.next = node # 也可以是 cur.next = self._head

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            # node.next = cur.next
            cur.next = node


    def insert(self, pos, item):
        # pos从0开始
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)

        else:
            node = Node(item)

            pre = self._head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return

        cur = self._head
        pre = None

        while cur.next != self._head:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self._head:
                    # 头节点
                    # 找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点，最后一个元素都是没有被处理过的
        if cur.elem == item:
            if cur == self._head:
                # 链表只有一个节点
                self._head = None
            else:
                pre.next = cur.next
                # pre.next = self._head

    def search(self, item):
        if self.is_empty():
            return False

        cur = self._head

        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True

        return False


if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
