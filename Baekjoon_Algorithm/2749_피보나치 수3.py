n = int(input())
a,b = 0,1
if n > 1500000:
    n %= 1500000
res = 0
for i in range(n-1):
    res = (a + b) %1000000
    a,b = b%1000000,res%1000000
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(res)
