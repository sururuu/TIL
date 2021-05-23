n = int(input())
if n == 0:
    print(0)
elif n > 0 or abs(n) % 2 == 1:
    print(1)
else:
    print(-1)

n = abs(n)
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a, b = 0, 1
    c = 0
    for i in range(n-1):
        c = (a + b) % 1000000000
        a = b % 1000000000
        b = c
    print(c)