# 이분 탐색
def sol():
    global res, case
    start, end = 0, k - 1
    while True:
        l = case[end] - case[start] + 1
        res = min(res, l)
        if end == len(case) - 1:
            break
        start += 1
        end += 1
    return res

n, k = map(int,input().split())
arr = list(map(int,input().split()))
res = 10**6 + 1
case = []
for i in range(n):
    if arr[i] == 1:
        case.append(i)
if len(case) < k:
    print(-1)
else:
    # sol2()
    for i in range(len(case)-k+1):
        res = min(res, case[i+k-1]-case[i]+1)
    print(res)
