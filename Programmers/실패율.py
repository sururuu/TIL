def solution(N, stages):
    answer = []
    fail = []
    l = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        fail.append(count)

    c = 0
    for stage in stages:
        if N < stage:
            c += 1
    fail.append(c)

    fail_r = []
    for i in range(N):
        if fail[i] == 0:
            fail_r.append((i + 1, 0))
        else:
            r = fail[i] / sum(fail[i:])
            fail_r.append((i + 1, r))
    fail_r = sorted(fail_r, key=lambda x: x[1], reverse=True)
    for k in range(len(fail_r)):
        answer.append(fail_r[k][0])
    return answer