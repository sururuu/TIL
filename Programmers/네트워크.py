def dfs(s, computers, visited):
    visited[s] = True
    for ind, j in enumerate(computers[s]):
        if visited[ind] == False and j == 1:
            dfs(ind, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * (n)

    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1
    return answer