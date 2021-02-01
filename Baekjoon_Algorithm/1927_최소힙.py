import heapq,sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            res = (heapq.heappop(heap))
            print(res)
        else:
            print(0)
    else:
        heapq.heappush(heap, num)

