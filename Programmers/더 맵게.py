import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        minimum1 = heapq.heappop(scoville)
        if minimum1 >= K:
            return answer
        if len(scoville) == 0:
            return -1
        minimum2 = heapq.heappop(scoville)
        heapq.heappush(scoville,minimum1+minimum2*2)
        answer += 1
