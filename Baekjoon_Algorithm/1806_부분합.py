n,s = map(int,input().split())
arr = list(map(int,input().split()))
ans = 100000
start,end = 0,0
num = 0
l = 0
while True:
    if num >= s:
        ans = min(ans,l)
        num -= arr[start]
        start += 1
        l -= 1
    elif end == len(arr):
        break
    else:
        num += arr[end]
        end += 1
        l += 1
if ans == 100000:
    print(0)
else:
    print(ans)