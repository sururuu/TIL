str1 = list(input())
str2 = list(input())
l = len(str1)
n = len(str2)
state = [[0]*(l+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,l+1):
        if str1[j-1] == str2[i-1]:
            state[i][j] = state[i-1][j-1] + 1
        else:
            state[i][j] = max(state[i-1][j],state[i][j-1])
print(state[-1][-1])