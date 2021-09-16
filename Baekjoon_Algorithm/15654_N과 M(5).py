def permutaion(k):
    if m == k:
        print(*res)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        res.append(arr[i])
        permutaion(k+1)
        visit[i] = False
        res.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [False] * n
res = []
permutaion(0)