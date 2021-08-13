def check(word):
    m = len(word) // 2
    left = word[:m]
    right = word[-m:]
    right.reverse()
    for i in range(m):
        if left[i] == right[i]:
            continue
        else:
            return False
    return True
s = list(input())
res = -1
if check(s):
    res = len(s) - 1
    if len(set(s)) == 1:
        res = -1
else:
    res = len(s)
print(res)