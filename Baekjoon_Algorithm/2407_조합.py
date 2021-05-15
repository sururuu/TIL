n,m = map(int,input().split())
m = min(m,n-m)
num = 1
if m == 0:
    print(num)
else:
    for i in range(n,n-m,-1):
        num *= i
    for i in range(1,m+1):
        num //= i
    print(num)