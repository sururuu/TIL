def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for heigt in range(1,total//2):
        width = 0
        if total % heigt == 0:
            width = total//heigt
            if width >= heigt:
                if brown == (width+heigt)*2 -4:
                    answer.append(width)
                    answer.append(heigt)
    return answer
