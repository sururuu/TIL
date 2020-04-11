def dfs(x):
    if x== M:
        print(*array)
        return
    for i in range(N):
        if check_number[i]:
            continue
        array.append(n_list[i])
        check_number[i] = True

        dfs(x+1)

        array.pop()
        check_number[i] = False



N,M = map(int,input().split())
n_list = [ _ for _ in range(1,N+1)]
check_number = [False]*(N)
array = []
dfs(0)