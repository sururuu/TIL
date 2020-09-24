n = int(input())

#sol1
def cnt(n):
    for x in range(n // 10 + 1):
        for y in range(n // 60 + 1):
            for z in range(n // 300 +1):
                if (10 * x + 60 * y + 300*z) == n:
                    return [z,y,x]
    return -1


#sol2
if n %10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = n//300
    b = (n%300) // 60
    c = (n%300) % 60 //10
    print(a,b,c)