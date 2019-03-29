# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素, O(1)
# append(item) 链表尾部添加元素, O(n)
# insert(pos, item) 指定位置添加元素, O(n)
# remove(item) 删除节点
# search(item) 查找结点是否存在, O(n)
# 链表失去了顺序表随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大，但对存储空间的使用相对灵活


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur != None:
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

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
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
        cur = self._head

        pre = None
        # while cur != None:
        while cur:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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
    ll = SingleLinkList()
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









