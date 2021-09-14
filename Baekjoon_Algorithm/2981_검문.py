from math import gcd, sqrt
n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()
diff = []
for i in range(1, n):
    diff.append(m[i] - m[i-1])
ans = diff[0]
for i in range(1, len(diff)):
    ans = gcd(ans, diff[i])
answer = []
for i in range(2, int(sqrt(ans))+1):
    if ans % i == 0:
        answer.append(i)
        answer.append(ans//i)
answer.append(ans)
answer = list(set(answer))
answer.sort()
print(*answer)