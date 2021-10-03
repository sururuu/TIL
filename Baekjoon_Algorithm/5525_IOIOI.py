n = int(input())
m = int(input())
s = input()
res, pn = 0, 0
idx = 0
while idx < m:
    if s[idx:idx+3] == 'IOI':
        pn += 1
        if pn == n:
            res += 1
            pn -= 1
        idx += 1
    else:
        pn = 0
    idx += 1
print(res)