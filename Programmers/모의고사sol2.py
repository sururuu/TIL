def solution(answers):
    answer = []
    q1 = [1,2,3,4,5]
    q2 = [2,1,2,3,2,4,2,5]
    q3 = [3,3,1,1,2,2,4,4,5,5]

    cnt = [0,0,0]

    for idx,res in enumerate(answers):
        if res == q1[idx%len(q1)]:
            cnt[0] += 1
        if res == q2[idx%len(q2)]:
            cnt[1] += 1
        if res == q3[idx%len(q3)]:
            cnt[2] += 1

    for idx, s in enumerate(cnt):
        if s == max(cnt):
            answer.append(idx+1)

    return answer
