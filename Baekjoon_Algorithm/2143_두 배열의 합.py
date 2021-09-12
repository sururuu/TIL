import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n):
    for j in range(i,n):
        s = sum(a[i:j+1])
        d[s] += 1
ans = 0
for i in range(m):
    for j in range(i,m):
        s = sum(b[i:j+1])
        ans += d[t-s]
print(ans)