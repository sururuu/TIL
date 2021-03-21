def solution(m, n, puddles):
    answer = 0
    Map = [[0]*(m+1) for _ in range(n+1)]
    # 출발지점
    Map[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            else:
                if [j,i] in puddles:
                    Map[i][j] = 0
                else:
                    Map[i][j] = Map[i-1][j] + Map[i][j-1]
    answer = Map[n][m]
    return answer % 1000000007