def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
dp = [0] * 1001
dp[1] = 3
for i in range(2,1001):
    cnt = 0
    for j in range(1, i):
        if gcd(i, j) == 1 :
            cnt += 1
    dp[i] = dp[i-1] + 2 * cnt
c = int(input())
for _ in range(c):
    n = int(input())
    print(dp[n])
