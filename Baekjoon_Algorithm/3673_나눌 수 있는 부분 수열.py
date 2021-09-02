import sys
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dp = [0]*d
    num = 0
    # dp는 나머지 합을 구한 배열
    for i in range(n):
        num += arr[i]
        num %= d
        dp[num] += 1
    # 나머지 배열에서
    # dp[k] 중 2개 선택 dp[k]C2
    for i in range(d):
        cnt += (dp[i]*(dp[i]-1)) // 2
    cnt += dp[0]
    print(cnt)