L, R = input().split()
Llen , Rlen = len(L), len(R)
cnt = 0
if Llen == Rlen:
    for i in range(Llen):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
print(cnt)