T = int(input())
for tc in range(1,T+1):
    L,U,X = map(int,input().split())
    time = 0
    if X > U:
        time = -1
    elif X < L:
        time = (L-X)
    print("#{} {}".format(tc,time))