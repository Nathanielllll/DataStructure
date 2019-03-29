result = []
def add(str1, str2, part):
    """字符串交换"""
    if str1 == "":
        result.append(part+str2)
        return
    if str2 == "":
        result.append(part+str1)
        return

    add(str1[1:], str2, part + str1[0])
    add(str1, str2[1:], part + str2[0])
    return
a = "AB"
b = "CD"
add(a, b, "")
print(result)