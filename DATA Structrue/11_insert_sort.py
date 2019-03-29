# alist = [93,          54,77,31,44,55,226]
# alist = [54,93,          77,31,44,55,226]
# alist = [54,77,93,          31,44,55,226]
## 把后面部分的第一个，插入到前面部分的正确位置
## 区分选择排序和插入排序的区别

# 对插入排序来说，是稳定的


# 最优时间复杂度为O(n^2)，最坏时间复杂度为O(n^2)
def insert_sort(alist):
    """"插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素，执行这样的过程
    for j in range(1, n):
        # j = [1,2,n-1]
        # i 代表内层循环起始值
        i = j
        # 内层循环执行从右边的无序序列第一个元素，即i位置的元素，插入到前面部分的正确位置
        while i>0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1 # i=j, j-1, j-2, ..., 1 和range(j, 0, -1)相同


# 改进的算法，提升最优时间复杂度，为O(n)，最坏时间复杂度仍然为O(n^2)
def insert_sort(alist):
    """"插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素，执行这样的过程
    for j in range(1, n):
        # j = [1,2,n-1]
        # i 代表内层循环起始值
        i = j
        # 内层循环执行从右边的无序序列第一个元素，即i位置的元素，插入到前面部分的正确位置
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1  # i=j, j-1, j-2, ..., 1 和range(j, 0, -1)相同
            else:
                break



if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    insert_sort(li)
    print(li)