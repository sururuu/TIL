def gcd(x,y):
    mod = x % y
    while mod:
        x, y = y, mod
        mod = x % y
    return y
a, b = map(int, input().split())
c, d = map(int, input().split())
num = gcd(a*d + c*b, b*d)
print((a*d + c*b)//num, b*d//num)