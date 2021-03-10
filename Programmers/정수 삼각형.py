def solution(triangle):
    answer = 0
    l = len(triangle)
    case = [[0]*(l+1) for _ in range(l+1)]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            case[i][j] = triangle[i][j]
    for i in range(1,l):
        for j in range(l):
            if j == 0:
                case[i][j] = case[i][j] + case[i-1][j]
            else:
                m = max(case[i][j]+case[i-1][j-1],case[i][j]+case[i-1][j])
                case[i][j] = m
    answer = (max(case[l-1]))
    return answer