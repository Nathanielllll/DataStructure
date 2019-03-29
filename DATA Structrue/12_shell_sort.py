# 希尔排序基于插入排序，是对子序列的插入排序
# 最优时间复杂度为O(n^1.3)，最坏时间复杂度为O(n^2)

# 不稳定的算法


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
# gap=1时，就是普通的插入排序，最坏时间复杂度为O(n^2)
    while gap>=1:
        gap//=2 # 控制gap的步长，gap变化到0之前，插入算法执行的次数
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, ..., n-1]
            # 与普通的插入算法的区别是gap步长
            # 通过一次循环，控制所有的子序列
            # 从gap开始，插入从1开始
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break



if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    shell_sort(li)
    print(li)