
# 비용산정
cost = []
for i in range(22):
    cost.append(i*i+(i-1)*(i-1))


t= int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    map_ = [list(map(int,input().split())) for _ in range(n)]

    # home 위치 저장하기 
    home=[]
    for i in range(n):
        for j in range(n):
            if map_[i][j] == 1:
                home.append((i,j))

    res = 0
    # 마름모의 중심 옮기면서 다니기
    for i in range(n):
        for j in range(n):
            cnt = [0]*(n+2)
            for p,q in home:
                dis = abs(i-p) + abs(j-q) + 1
                if dis <= n+1:
                    cnt[dis] += 1
            for k in range(1,n+2):
                cnt[k] += cnt[k-1]
                if cnt[k]*m >= cost[k]:
                    if res < cnt[k]:
                        res = cnt[k]
    print("#{} {}".format(tc,res))