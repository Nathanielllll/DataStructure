# 冒泡排序是稳定的

## 时间复杂度为O(n^2)
# def bubble_sort(alist):
#     """冒泡排序"""
#     n = len(alist)
#     for j in range(0, n-1):
#         for i in range(0, n-1-j): # 0~n-2
#             # 代表一次循环
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]



## 改进：如果有序，直接退出，最优时间复杂度为O(n)，最坏时间复杂度仍然为O(n^2)
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n-1):
        count = 0
        for i in range(0, n-1-j): # 0~n-2
            # 代表一次循环
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return



if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    bubble_sort(li)
    print(li)