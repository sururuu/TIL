n = int(input())
s = list(input())
start = 0
res = 0
word = {}
for i in range(len(s)):
    if s[i] not in word:
        word[s[i]] = 1
    else:
        word[s[i]] += 1
    if len(word) > n:
        while len(word) > n:
            word[s[start]] -= 1
            if word[s[start]] == 0:
                del word[s[start]]
            start += 1
    cnt = sum(word.values())
    res = max(res,cnt)
print(res)