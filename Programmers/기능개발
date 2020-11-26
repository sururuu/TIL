def solution(progresses, speeds):
    answer = []
    new = []
    # testcase 1개가 틀린이유 number 가 모두 정수라 가정 하여 오류 해결
    for i in range(len(progresses)):
        number = (100 - progresses[i]) / speeds[i]
        if number.is_integer():
            pass
        else:
            number = (100 - progresses[i]) // speeds[i] + 1
        new.append(number)
    print(new)
    while new:
        cnt = 0
        delete_list = []
        for i in range(len(new)):
            if new[i] == 0:
                pass
            else:
                new[i] -= 1

        for i in range(len(new)):
            if new[i] == 0:
                cnt += 1
                delete_list.append(i)
            elif new[i] != 0:
                break
        if len(delete_list) > 0:
            new = new[len(delete_list):]
            answer.append(cnt)
    return answer
