n = int(input())
h = list(map(int, input().split()))
cnt = 0
visit = [0] * (n+1)
for b in h:
    if not visit[b]:
        cnt += 1
        visit[b-1] += 1
    else:
        visit[b] -= 1
        visit[b-1] += 1
print(sum(visit))