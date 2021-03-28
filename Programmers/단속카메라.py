def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = -30000
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer