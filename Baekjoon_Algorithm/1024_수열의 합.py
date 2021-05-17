N,L = map(int,input().split())
x = -1
start = 0
l = 0
for i in range(L,101):
    t = (i*i-i)//2
    if (N-t) % i == 0 and (N-t) // i >=0:
        x = (N-t)//i
        start = x
        l = i
        break
if x == -1:
    print(-1)
else:
    for i in range(start,start+l):
        print(i,end=' ')

# n = x + (x+1) + ``` + (x+l-1)
# n = lx + (l(l-1))/2
# t = (l((l-1))/2
# n = lx + t
# x = (n-t)/l
