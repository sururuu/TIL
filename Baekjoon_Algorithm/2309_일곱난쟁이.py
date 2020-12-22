men = [int(input()) for _ in range(9)]
Sum = sum(men)
men.sort()
res = []
for i in range(8):
    for j in range(i+1,9):
        if (Sum - men[i] - men[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(men[k])
            exit()
