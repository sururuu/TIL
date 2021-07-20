import heapq
def solution(data):
    left, right = [], []
    mid = data[0]
    res = [mid]
    for idx, val in enumerate(data[1:],1):
        if val > mid:
            heapq.heappush(right,val)
        else:
            heapq.heappush(left, -val)
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right,mid)
                mid = -heapq.heappop(left)
            res.append(mid)
    print(len(res))
    for i in range(len(res)):
        if (i+1) != 1 and (i+1) % 10 == 1:
            print()
        print(res[i], end=' ')
    print()
t = int(input())
for tc in range(t):
    m = int(input())
    data = []
    if m % 10 == 0:
        data.extend(list(map(int,input().split())))
    else:
        for _ in range(m//10 + 1):
            data.extend(list(map(int,input().split())))
    solution(data)