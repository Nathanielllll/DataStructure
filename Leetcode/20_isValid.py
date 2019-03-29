def isValid(s):
    lookup = {'(': ')', '{': '}', '[': ']'}
    temp = []
    for str in s:
        if str in lookup:
            temp.append(str)
        elif len(temp) == 0 or str != lookup[temp.pop()]:
            return False
    return len(temp) == 0

