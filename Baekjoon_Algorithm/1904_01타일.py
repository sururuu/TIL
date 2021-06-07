n = int(input())
a, b = 1, 2
res = 0
for i in range(n-2):
    res = (a+b) % 15746
    a, b = b % 15746, res
if n == 1:
    res = a
elif n == 2:
    res = b
print(res % 15746)