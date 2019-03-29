def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            minCoins = min(numCoins, minCoins)
    return minCoins

# print(recMC([1,5,10,25],63))


# 我们所做的不是动态规划，而是我们通过使用称为"记忆化"的技术来提高我们的程序的性能，或者更常见的叫做"缓存"。
def recDC(coinValueList, change, knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   # 看看我们的列表是否包含此找零的最小硬币数量。
   # 如果没有，我们递归计算最小值，并将计算出的最小值存储在列表中
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

# print(recDC([1,5,10,25],63,[0]*64))


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    return minCoins[change]
















