while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    arr = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
    res = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j]:
                s = min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1])
                if s:
                    arr[i][j] += s
                    res = max(res, arr[i][j])
                else:
                    res = max(res,1)
    print(res)