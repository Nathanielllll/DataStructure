# 使用目标杆将 n-1 的塔移动到中间杆。
# 将剩余的盘子移动到目标杆。
# 使用起始杆将 n-1 的塔从中间杆移动到目标杆。


def hanoi(n, start, mid, end):

    if n == 1:
        print("从"+start+"移到"+end)
    else:
        hanoi(n-1, start, end, mid)
        print("从"+start+"移到"+end)
        hanoi(n-1, mid, start, end)

# def hanoi(n,a,b,c):
#     # if n < 0:
#     #     print('enter n >0')
#     if n==1:
#         print(a,'-->',b)
#     else:
#         hanoi(n-1,a,c,b)
#         print(a,'-->',b)
#         hanoi(n-1,b,a,c)


hanoi(2, "A", "B", "C")
