n, l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start = arr[0]
cnt = 1
for i in range(1,n):
    if arr[i] - start <= l-1:
        continue
    else:
        cnt += 1
        start = arr[i]
print(cnt)