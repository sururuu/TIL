def dfs(idx, num):
    global case
    if idx == n:
        return
    case.add(num + s[idx])
    dfs(idx+1, num + s[idx])
    dfs(idx+1, num)

n = int(input())
s = list(map(int, input().split()))
ans = 0
case = set(s[:])
dfs(0, 0)
m = max(case)
for i in range(m):
    if i+1 not in case:
        print(i+1)
        exit()
print(m+1)