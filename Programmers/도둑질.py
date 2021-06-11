def solution(money):
    answer = 0
    dp = [0]*len(money)
    # 첫 번째 집을 터는 경우
    dp[0:2] = money[0], money[0]
    for i in range(2,len(money)-1):
        dp[i] = max(dp[i-1],dp[i-2]+money[i])
        answer = max(answer,dp[i])
    # 마지막 집을 터는 경우
    dp[0:2] = 0, money[1]
    for i in range(2,len(money)):
        dp[i] = max(dp[i-1],dp[i-2]+money[i])
        answer = max(answer,dp[i])
    return answer