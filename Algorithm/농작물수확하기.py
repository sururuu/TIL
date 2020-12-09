T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    n_list = [list(map(int, input())) for i in range(n)]
    result_sum = 0
    result_list = []
    y = [i for i in range(int(n / 2), -1, -1)]
    y2 = [i for i in range(int(n / 2), 0, -1)]

    for i in range(int(n / 2) + 1):
        y_end = y[i] + 2 * i + 1
        res = (n_list[i][y[i]:y_end])
        result_list.append(res)

    jj = 0
    for i in range(n - 1, int(n / 2), -1):
        y_end = y[jj] + 2 * jj + 1
        res = (n_list[i][y2[jj]:y_end])
        jj += 1
        result_list.append(res)

    for i in range(n):
        result_sum += sum(result_list[i])

    print("#{0} {1}".format(tc, result_sum))