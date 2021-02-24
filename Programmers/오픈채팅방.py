def solution(record):
    ans = []
    answer = []
    res = {}
    for i in range(len(record)):
        record[i] = record[i].split(' ')
        if "Enter" in record[i]:
            answer.append([record[i][1], "님이 들어왔습니다."])
            res[record[i][1]] = record[i][2]
        elif "Leave" in record[i]:
            answer.append([record[i][1], "님이 나갔습니다."])
        else:
            res[record[i][1]] = record[i][2]

    for i in range(len(answer)):
        ans.append(res[answer[i][0]]+answer[i][1])
    return ans