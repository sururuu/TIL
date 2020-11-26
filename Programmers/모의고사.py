import copy
def solution(answers):
    answer = []
    q1 = [1,2,3,4,5]
    q2 = [2,1,2,3,2,4,2,5]
    q3 = [3,3,1,1,2,2,4,4,5,5]
    l = len(answers)
    answersCopy = copy.deepcopy(answers)
    for k in [q1,q2,q3]:
        cnt = 0
        while answers:
            for i in range(len(answers)):
                if answers[i] == k[i]:
                    answers.pop(0)
                    k.append(k[i])
                    k.pop(0)
                    cnt += 1
                    break
                else:
                    answers.pop(0)
                    k.append(k[i])
                    k.pop(0)
                    break
        answers = copy.deepcopy(answersCopy)
        answer.append(cnt)
    Max = max(answer)
    result = []
    for i in range(len(answer)):
        if answer[i] == Max:
            result.append(i+1)

    return result

