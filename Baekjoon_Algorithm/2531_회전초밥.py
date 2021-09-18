from collections import defaultdict
def sol1():
    res = 0
    for i in range(n):
        case = list(set(sushi[i:i+k]))
        cnt = len(case)
        if c not in case:
            cnt += 1
        if cnt == k+1:
            res = k + 1
            break
        res = max(res, cnt)
    return res
def sol2():
    dict = defaultdict(int)
    dict[c] = 1
    for i in range(k):
        dict[sushi[i]] += 1
    cnt = len(dict)
    ans = cnt
    for i in range(k, len(sushi)):
        prev = sushi[i-k]
        temp = sushi[i]
        if prev == temp:
            continue
        else:
            dict[prev] -= 1
            dict[temp] += 1
            if dict[prev] == 0:
                cnt -= 1
            if dict[temp] == 1:
                cnt += 1
        ans = max(ans, cnt)
        if ans == k+1:
            break
    return ans
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
plus = sushi[:k-1]
sushi += plus
print(sol2())
