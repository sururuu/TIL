def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
n, s = map(int,input().split())
arr = list(map(int,input().split()))
a = abs(s-arr[0])
res = a
for i in range(1,n):
    res = gcd(res, abs(s-arr[i]))
print(res)