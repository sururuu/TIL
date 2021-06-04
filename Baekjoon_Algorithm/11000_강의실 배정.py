import heapq
n = int(input())
case = [list(map(int,input().split())) for _ in range(n)]
case = sorted(case,key=lambda x:(x[0],x[1]))
end_time = []
for i in range(n):
    if end_time and end_time[0] <= case[i][0]:
        heapq.heappop(end_time)
    heapq.heappush(end_time,case[i][1])
print(len(end_time))

# for i in range(n):
#     if end_time and min(end_time) <= case[i][0]:
#         end_time.remove(min(end_time))
#     end_time.append(case[i][1])
# 시간 초과나는 코드 -> heapq를 사용해서 해결