import sys
t = int(input())
for tc in range(t):
    error = False
    p = input()
    n = int(input())
    x = sys.stdin.readline()[1:-2].split(',')
    reversCnt = 0
    removeCnt = 0
    for fun in p:
        if fun == 'R':
             reversCnt += 1
        else:
            if len(x) == 0 or n == 0:
                error = True
                break
            if reversCnt % 2 == 0:
                removeCnt += 1
            else:
                x.pop()
    if error or removeCnt > len(x):
        print('error')
    else:
        x = x[removeCnt:]
        if reversCnt % 2 == 1 :
            x.reverse()

        print("[", end='')
        for i in range(len(x)):
            if i == len(x) - 1:
                print(x[i],end='')
            else:
                print(x[i],end=',')
        print("]")