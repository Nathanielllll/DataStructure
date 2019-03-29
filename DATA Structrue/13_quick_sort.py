# 最优时间复杂度为O(nlogn)，最坏时间复杂度为O(n^2)
# 不稳定，移动的过程当中会跳

def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:  # 使用>=是为了和mid_value相同的值放在同一边
            high -= 1
        alist[low] = alist[high]

        # low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    # 从循环退出，low==high
    alist[low] = mid_value

    # 对low左边的列表进行快速排序，函数调用自身，使用了递归
    quick_sort(alist, first, low-1)

    # 对low右边的列表进行快速排序
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)