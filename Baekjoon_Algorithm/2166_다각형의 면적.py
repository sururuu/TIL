n = int(input())
x1, y1 = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n-1)]
s = 0
for i in range(n-2):
    x2, y2 = arr[i]
    x3, y3 = arr[i+1]
    s += (x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)
s = abs(s)/2
print(round(s,1))