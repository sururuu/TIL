from _collections import deque
a,b = map(int,input().split())
res = -1
q = deque()
q.append((a,1))
while q:
    num,cnt = q.popleft()
    if num == b:
        res = cnt
        print(res)
        exit()
    if num * 2 <= b:
        q.append((num*2,cnt+1))
    if int(str(num)+'1') <= b:
        q.append((int(str(num)+'1'),cnt+1))
print(res)