n, m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
s = [0 for _ in range(m)]
num = 0
# i번째 자리까지의 합 구해서 나머지 s에 넣기
for i in range(n):
    num += a[i]
    num %= m
    s[num] += 1
# s[4] - s[1] = a[2] + a[3]
# 각각의 나머지마다 2개씩 뽑아서 더하기 nC2
for i in range(m):
    cnt += (s[i]*(s[i]-1)) // 2
cnt += s[0]
print(cnt)