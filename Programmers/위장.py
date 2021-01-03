def solution(clothes):
    answer = 0
    arrs = {}
    for i in range(len(clothes)):
        clothe, index = clothes[i]
        if index not in arrs:
            arrs[index] = 1
        else:
            arrs[index] += 1

    count = 1
    for key, arr in arrs.items():
        count *= (arr + 1)

    answer = count - 1
    return answer