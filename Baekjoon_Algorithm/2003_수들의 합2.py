import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
start,end = 0,0
num = 0
while True:
    if num >= m:
        num -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        num += arr[end]
        end += 1
    if num == m:
        cnt += 1
print(cnt)

# 투포인터 
