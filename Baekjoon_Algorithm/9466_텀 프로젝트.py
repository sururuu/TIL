import sys
sys.setrecursionlimit(100000)
def dfs(idx):
    global cycle,cnt
    visit[idx] = True
    cycle.append(idx)
    next_idx = arr[idx]
    if not visit[next_idx]:
        dfs(next_idx)
    else:
        # 싸이클 찾기
        # 마지막에 끝나는 값과 첫번째 인덱스 값이 같아야 싸이클!
        # 싸이클 길이만큼 더해주기
        if next_idx in cycle:
            index = cycle.index(next_idx)
            cycle = cycle[index:]
            cnt += len(cycle)

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visit = [False] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visit[i]:
            cycle = []
            dfs(i)
    # 싸이클에 들어오지 못한 값들의 길이
    # 원래 길이에서 싸이클 길이를 빼기
    print(n-cnt)
