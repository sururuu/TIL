import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    arr.append([0] + list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1, m+1):
        arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    s = 0
    s += arr[x2][y2]
    s -= arr[x1-1][y2]
    s -= arr[x2][y1-1]
    s += arr[x1-1][y1-1]
    print(s)