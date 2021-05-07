s1 = input()
s2 = input()
res = 0
result = ''
dp = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
word = dp[-1][-1]
if word:
    print(len(word))
    print(word)
else:
    print(0)
