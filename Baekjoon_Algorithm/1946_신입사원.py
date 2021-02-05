import sys
t = int(input())
for tc in range(t):
    n = int(input())
    score = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
    score.sort()
    people = 1
    m = score[0][1]
    for i in range(1,n):
        if m > score[i][1]:
            people += 1
            m = score[i][1]
    print(people)