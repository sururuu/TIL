def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    num = 1
    target = sum([i for i in range(1, n + 1)])
    for i in range(n):
        if num > target:
            break
        # 아래로
        if i % 3 == 0:
            while True:
                answer[x][y] = num
                num += 1
                if x + 1 < n and answer[x + 1][y] == 0:
                    x += 1
                else:
                    y += 1
                    break
        # 오른쪽으로
        if i % 3 == 1:
            while True:
                answer[x][y] = num
                num += 1
                if y + 1 < n and answer[x][y + 1] == 0:
                    y += 1
                else:
                    x -= 1
                    y -= 1
                    break
        # 왼쪽 대각선 위로
        if i % 3 == 2:
            while True:
                answer[x][y] = num
                num += 1
                if answer[x - 1][y - 1] == 0:
                    x -= 1
                    y -= 1
                else:
                    x += 1
                    break
    ans = []
    for i in range(n):
        for j in range(n):
            if answer[i][j] != 0:
                ans.append(answer[i][j])

    return ans