import heapq
from sys import stdin
n = int(stdin.readline())
heap = []
for i in range(n):
    num = int(stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
