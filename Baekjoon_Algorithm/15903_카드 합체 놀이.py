import heapq
n, m = map(int,input().split())
a = list(map(int,input().split()))
def sol():
    global m
    while m:
        m -= 1
        a.sort()
        s = a[0] + a[1]
        a[:2] = [s,s]
    return sum(a)
def sol_2():
    global m
    heapq.heapify(a)
    for i in range(m):
        card1 = heapq.heappop(a)
        card2 = heapq.heappop(a)
        s = card1 + card2
        heapq.heappush(a,s)
        heapq.heappush(a,s)
    return sum(a)
print(sol_2())