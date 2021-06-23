import sys
n = int(input())
arr = list(map(int,input().split()))
start, end = 0, n-1
num = 0
res = []
m = sys.maxsize
while start < end:
    s = arr[start] + arr[end]
    if m > abs(s):
        m = abs(s)
        res = [arr[start], arr[end]]
    if s > 0:
        end -= 1
    elif s < 0:
        start += 1
    else:
        break
print(*res)