import heapq
n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
s = 0
if n == 1:
    print(0)
else:
    while cards:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        c = a + b
        if cards:
            heapq.heappush(cards, c)
        s += c
    print(s)
