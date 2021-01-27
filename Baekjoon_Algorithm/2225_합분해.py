n,k = map(int,input().split())
# 2H20
# kHn
# (k+n-1)Cn
# (k+n-1)!/(k-1)!*n!
def fac(num):
    s = 1
    for i in range(num,0,-1):
        s *= i
    return s
res = fac(k+n-1)//((fac(k-1))*fac(n))
res = (res % 1000000000)
print(res)