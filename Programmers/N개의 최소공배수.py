def solution(arr):
    answer = 0
    m = max(arr)
    M = 1
    l = len(arr)
    for i in range(l):
        M *= arr[i]
    for i in range(m,M+1):
        cnt = 0
        for j in range(l):
            if i % arr[j] != 0:
                break
            else:
                cnt += 1
        if cnt == l:
            return i
    return answer