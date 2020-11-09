#  python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다.
#  sys.setrecursionlimit(10000) 작성
# input 보다 sys 가 속도가 더 빠르기 때문에 런타임에러가 생겨 사용함. 
import sys
sys.setrecursionlimit(10000)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(s):
    visited[s] = True
    for i in graph[s]:
        if visited[i] == False:
            dfs(i)

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)