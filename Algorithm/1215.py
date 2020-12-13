def solution(table):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            new = table[i][j:j+n]
            mid = len(new)//2
            length = len(new)
            check = 0
            for k in range(mid):
                if new[k] == new[length-1-k]:
                    check += 1
                else:
                    break
            if check == mid :
                cnt += 1
    return cnt

for tc in range(1,11):
    n = int(input())
    table = [list(input()) for i in range(8)]
    res = 0

    #가로
    res += solution(table)
    #세로
    new_table = list(map(list,zip(*table)))
    res += solution(new_table)

    print("#{} {}".format(tc,res))