from collections import deque
def solution(priorities, location):
    answer = 0
    d = deque()
    for i in range(len(priorities)):
        d.append((priorities[i],i))
    while True:
        first = d.popleft()
        if d and max(d)[0] > first[0]:
            d.append(first)
        else:
            answer += 1
            if first[1] == location:
                break
    return answer