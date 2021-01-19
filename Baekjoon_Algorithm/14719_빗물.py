h,w = map(int,input().split())
table = list(map(int,input().split()))
drop = 0
for i in range(1,w-1):
    left = max(table[:i])
    right = max(table[i+1:])
    water = min(left,right)
    if table[i] < water:
        drop += abs(table[i]-water)
print(drop)