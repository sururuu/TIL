n = int(input())
h = list(map(int,input().split()))
s = sum(h)
turn = s // 3
if s % 3 != 0:
    print('NO')
else:
    cnt = 0
    for i in range(n):
        if h[i] % 2 == 1:
            cnt += 1
    if cnt <= turn:
        print('YES')
    else:
        print('NO')
