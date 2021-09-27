import math
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = []
for i in range(n-k+1):
    for j in range(i+k, n+1):
        case = arr[i:j]
        avg = sum(case)/len(case)
        s = 0
        for p in range(0, len(case)):
            s += (case[p]-avg)**2
        s /= len(case)
        res.append(s)
print(math.sqrt(min(res)))