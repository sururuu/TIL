from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    for city in cities:
        city = city.lower()
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            if len(q) >= cacheSize:
                q.popleft()
            answer += 5
            q.append(city)


    return answer