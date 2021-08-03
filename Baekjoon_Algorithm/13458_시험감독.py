import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
res = n
for i in range(n):
    room = a[i]
    room -= b
    if room > 0:
        q, r = divmod(room, c)
        res += q
        if r:
            res += 1
print(res)