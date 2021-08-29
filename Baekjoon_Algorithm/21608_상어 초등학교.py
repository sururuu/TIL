import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
dic = defaultdict(list)
arr = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0
for _ in range(n**2):
    _arr = list(map(int, input().split()))
    idx = _arr[0]
    dic[idx] = _arr[1:]
    max_x, max_y = 0, 0
    max_like, max_empty = -1, -1
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                like, empty = 0, 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in _arr[1:]:
                            like += 1
                        if not arr[nx][ny]:
                            empty += 1
                # 해당 칸에 좋아하는 친구가 더 많거나
                # 친구수가 같다면 주변에 빈칸이 더 많은 경우 자리 업데이트
                if max_like < like or (max_like == like and max_empty < empty):
                    max_x, max_y = i, j
                    max_like = like
                    max_empty = empty
    arr[max_x][max_y] = idx
for i in range(n):
    for j in range(n):
        cnt = 0
        idx = arr[i][j]
        like = dic[idx]
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in like:
                    cnt += 1
        if cnt:
            res += 10**(cnt-1)

print(res)