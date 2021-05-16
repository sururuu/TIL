import heapq
k,n = map(int,input().split())
arr = list(map(int,input().split()))
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,arr[i])
res = 0
for i in range(n):
    num = heapq.heappop(heap)
    for j in range(k):
        heapq.heappush(heap,num*arr[j])
        # 2*3 3*2 중복방지
        if num % arr[j] == 0:
            break
    res = num
print(res)

#    2  3  5 
# 2  4  6  10
# 3  6  9  15
# 5  10 15 25
# 대각선을 기준으로 값이 동일(중복된 숫자가 생김)
# 대각선 아래 삼각형을 기준으로 heap 에 값 넣기