from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [],[],[],[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = defaultdict(int)
for i in range(n):
    for j in range(n):
        s = A[i] + B[j]
        AB[s] += 1

cnt = 0
for i in range(n):
    for j in range(n):
        s = -(C[i] + D[j])
        if s in AB:
            cnt += AB[s]
print(cnt)