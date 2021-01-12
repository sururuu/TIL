n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]
# 아래줄부터 큰수 더해서 저장하기
for i in range(n-2,-1,-1):
    for j in range(len(triangle[i])):
        m = max(triangle[i+1][j],triangle[i+1][j+1])
        triangle[i][j] += m

print(triangle[0][0])