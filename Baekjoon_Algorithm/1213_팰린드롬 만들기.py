words = list(input())
words.sort()
alpha = {i: 0 for i in range(65, 91)}
for word in words:
    alpha[ord(word)] += 1
res = ''
other = ''
flag = True
status = True
for target in alpha:
    idx = alpha[target]
    if idx > 0:
        if idx % 2 == 0:
            r = idx // 2
            res += chr(target) * r
            alpha[target] = 0
        else:
            if not flag:
                status = False
                break
            flag = False
            r, q = divmod(idx, 2)
            res += chr(target) * r
            other += chr(target)
            alpha[target] = 0
if not status:
    res = "I'm Sorry Hansoo"
else:
    res = res + other + res[::-1]
print(res)
