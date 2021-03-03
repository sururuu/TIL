import heapq
n = int(input())
q = []
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        num = arr[j]
        heapq.heappush(q,(num))
        if len(q) > n:
            while len(q)>n:
                heapq.heappop(q)
print(q[0])