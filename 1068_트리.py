def solve(target,arr):
    arr[target] = -2
    for i in range(n):
        if arr[i] == target:
            solve(i,arr)

n = int(input())
arr = list(map(int,input().split()))
target = int(input())

solve(target,arr)
cnt = 0
for i in range(n):
    num = arr[i]
    if arr[i] != -2:
        if i not in arr:
            cnt += 1
print(cnt)