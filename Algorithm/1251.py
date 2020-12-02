import heapq

N = int(input())
island = []
x = list(map(int,input().split()))
y = list(map(int,input().split()))
E = (input())
for i in range(N):
    xx = x[i]
    yy = y[i]
    island.append([xx,yy])
dis = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        x1 = island[i][0]
        y1 = island[i][1]
        x2 = island[j][0]
        y2 = island[j][1]
        d = (x1-x2)**0.5 + (y1-y2)**2
        dis[i][j] = d
print(dis)