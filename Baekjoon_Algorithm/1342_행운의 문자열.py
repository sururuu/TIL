def dfs(depth, string):
    global char, charSet, cnt, lenght
    if depth == lenght:
        cnt += 1
        return
    for target in charSet:
        idx = ord(target) - ord('a')
        if char[idx] == 0:
            continue
        if string and string[-1] == target:
            continue
        char[idx] -= 1
        dfs(depth+1, string+target)
        char[idx] += 1

s = input()
char = [0] * 26
charSet = set()
cnt = 0
lenght = len(s)
for target in s:
    idx = ord(target) - ord('a')
    char[idx] += 1
    charSet.add(target)
dfs(0, '')
print(cnt)