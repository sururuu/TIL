from collections import deque
n = int(input())
arr = list(map(int,input().split()))
res = [-1]*n
stack = deque()
stack.append(0)
for i in range(1,n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        res[idx] = arr[i]
    stack.append(i)
print(*res)