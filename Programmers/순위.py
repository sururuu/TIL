def solution(n, results):
    answer = 0
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = '-1'
    for res in results:
        x, y = res
        dp[x-1][y-1] = 'win'
        dp[y-1][x-1] = 'lose'
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] == 'win' and dp[k][j] == 'win':
                    dp[i][j] = 'win'
                if dp[i][k] == 'lose' and dp[k][j] == 'lose':
                    dp[i][j] = 'lose'
    for i in range(n):
        if dp[i].count('win') + dp[i].count('lose') == n-1:
            answer += 1
    return answer