def prime(n):
    arr = [True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False
    prime_arr = []
    for i in range(2, n+1):
        if arr[i]:
            prime_arr.append(i)
    return prime_arr

n = int(input())
arr = prime(n)
dp = [0]*(n+1)
dp[0] = 1
for i in arr:
    for j in range(i, n+1):
        dp[j] = (dp[j] + dp[j-i]) % 123456789
print(dp[n] % 123456789)

# 에라토스테네스의 체
# 동전 문제 유사