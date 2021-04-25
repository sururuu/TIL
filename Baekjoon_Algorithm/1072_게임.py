x,y = map(int,input().split())
z = int(100*y/x)
cnt = 0
if z >= 99:
    print(-1)
    exit()
start,end = 0,1000000000
while start <= end:
    mid = (start+end)//2
    if int(100*(y+mid)/(x+mid)) > z:
        cnt = mid
        end = mid - 1
    else:
        start = mid + 1

print(cnt)
