t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    n_list = [list(map(int, input().split())) for i in range(n)]
    res = []

    for i in range(n):
        for j in range(n):
            if n_list[i][j] != 0:
                # 옆으로
                row = 0
                y = j
                while y < n:
                    if n_list[i][y] != 0:
                        row += 1
                        y += 1
                    else:
                        break
                # 밑으로
                line = 0
                x = i
                while x < n:
                    if n_list[x][j] != 0:
                        line += 1
                        x += 1
                    else:
                        break
                res.append([line * row, line, row])
                # 0으로
                for dx in range(i, x):
                    for dy in range(j, y):
                        n_list[dx][dy] = 0
    # 정렬
    res.sort(key=lambda x: (x[0], x[1]))
    print("#{0} {1}".format(tc, len(res)), end=' ')
    for i in range(len(res)):
        for j in range(1, len(res[i])):
            print(res[i][j], end=' ')
    print()