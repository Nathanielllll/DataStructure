
def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for string in strs[1:]:
            if len(string) <= i or strs[0][i] != string[i]:
                # 默认前面都是相同的。一旦不同，则返回[:i]的元素
                return strs[0][:i]

    return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))