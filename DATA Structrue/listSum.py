# 递归算法必须具有基本情况。-->停止条件
# 递归算法必须改变其状态并向基本情况靠近。
# 递归算法必须以递归方式调用自身。

def listSum(list):

    if len(list) == 1:
        return list[0]
    else:
        return list[0] + listSum(list[1:])

print(listSum([1,2,3,5,5]))
