n,m = map(int,input().split())
nemo = [list(map(int,input())) for _ in range(n)]
def square(n,m,nemo):
    # (1,1) 부터 시작
    # 왼, 위, 왼쪽 위 대각선
    for i in range(1,n):
        for j in range(1,m):
            if nemo[i][j] > 0:
                case1 = nemo[i][j-1]
                case2 = nemo[i-1][j]
                case3 = nemo[i-1][j-1]
                Min = min(case1,case2,case3)
                if Min != 0 :
                    nemo[i][j] += Min
    Max = max(map(max,nemo))
    return Max**2
print(square(n,m,nemo))