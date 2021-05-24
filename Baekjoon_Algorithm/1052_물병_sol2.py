n, k = map(int,input().split())
res = 0
while bin(n).count('1') > k:
    s = bin(n)[::-1].index('1')
    cnt = 2 ** s
    res += cnt
    n += cnt
print(res)