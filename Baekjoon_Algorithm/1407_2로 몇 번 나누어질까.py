def solve(n):
    ans, temp = 0, 1
    while n:
        if n % 2 == 0:
            ans += (n//2)*temp
        else:
            ans += (n//2+1)*temp
        n //= 2
        temp *= 2
    return ans
a,b = map(int,input().split())
res = 0
# F(9) - F(4) = 21 - 8 = f(5) + ``` + f(9)
# F(9) = 5*1 + 2*2 + 1*4 + 1*8
res = solve(b) - solve(a-1)
print(res)