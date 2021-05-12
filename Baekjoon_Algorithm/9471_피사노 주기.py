p = int(input())
for tc in range(p):
    n,m = map(int,input().split())
    a,b = 1, 1
    cnt = 0
    while True:
        c = (a + b) % m
        a = b
        b = c
        cnt += 1
        if a == 1 and b == 1:
            break
    print(n,cnt)