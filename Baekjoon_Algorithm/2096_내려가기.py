import sys
n = int(input())
arr = []
maxN = [[0 for _ in range(3)] for _ in range(2)]
minN = [[0 for _ in range(3)] for _ in range(2)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))

    maxN[1][0] = max(maxN[0][0],maxN[0][1]) + temp[0]
    minN[1][0] = min(minN[0][0],minN[0][1]) + temp[0]

    maxN[1][1] = max(maxN[0][0],maxN[0][1],maxN[0][2]) + temp[1]
    minN[1][1] = min(minN[0][0],minN[0][1],minN[0][2]) + temp[1]

    maxN[1][2] = max(maxN[0][1],maxN[0][2]) + temp[2]
    minN[1][2] = min(minN[0][1],minN[0][2]) + temp[2]

    for k in range(3):
        maxN[0][k] = maxN[1][k]
        minN[0][k] = minN[1][k]

print(max(maxN[1]),min(minN[1]))