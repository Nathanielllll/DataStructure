# alist = [    54,226,93,17,77,31,44,55,20]
# alist = [17,    226,93,54,77,31,44,55,20]
# alist = [17,20,    93,54,77,31,44,55,226]
# alist = [17,20,31,    54,77,93,44,55,226]
## 分成两部分，从后面的一部分选出最小的一个，放到前面的一部分

# 对选择排序来说，是不稳定的（考虑升序每次选择最大的情况）
# 而冒泡排序是稳定的
# 例子如下所示：(26,1)和(26,2)交换了位置
# li = [(26,2),16,17,15,(26,1),11,9]
# li = [9,16,17,15,(26,1),11,(26,2)]
# li = [9,16,17,15,11,(26,1),(26,2)]


## 没有找到更优的方式，时间复杂度都为O(n^2)
def select_sort(alist):
    """"选择排序"""
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]




if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    select_sort(li)
    print(li)
