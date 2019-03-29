# 先操作node，尽量不打断原有的list的内部关系

class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head is None
        # return self._head == None
    def length(self):
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        # pos从0开始
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)

        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当cur退出循环，cur指向pos位置
            node = Node(item)

            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            # 后两个也可以写成下列方式：
            # cur.pre = node
            # node.prev.next = node

    def remove(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self._head:
                    # 头节点
                    self._head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 判断是否为链表最后一个节点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = DoubleLinkList()
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
