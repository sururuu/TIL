import heapq
def solution(operations):
    answer = []
    for operation in operations:
        target = list(operation.split(' '))
        if target[0] == 'I':
            heapq.heappush(answer,int(target[1]))
        else:
            if answer:
                # 최댓값 삭제
                if '1' == target[1]:
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                # 최솟값 삭제
                else:
                    heapq.heappop(answer)
    ans = []
    if not answer:
        ans = [0,0]
    else:
        ans.append(heapq.nlargest(1,answer)[0])
        ans.append(heapq.heappop(answer))
    return ans