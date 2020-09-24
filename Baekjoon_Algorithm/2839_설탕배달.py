n = int(input())

# sol1
res = n
for x in range(n//3+1):
    for y in range(n//5+1):
        if (3*x+5*y) == n :
            if (x+y) < res:
                res = x+y
if res == n:
    res = -1

# sol2

def cnt(n):
    for x in range(n // 3 + 1):
        for y in range(n // 5 + 1):
            if (3 * x + 5 * y) == n:
                return x+y
    return -1

print(cnt(n))