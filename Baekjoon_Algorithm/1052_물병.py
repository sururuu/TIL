n, k = map(int,input().split())
check = [2**i for i in range(25)]
res = 0
if n in check or n < k:
    print(0)
else:
    binN = bin(n)
    cnt = binN.count('1')
    while True:
        if cnt <= k:
            break
        n += 1
        binN = bin(n)
        cnt = binN.count('1')
        res += 1
    print(res)