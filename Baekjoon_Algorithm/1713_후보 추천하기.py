n = int(input())
c = int(input())
person = list(map(int,input().split()))
p = []
vote = []
for i in range(c):
    # 이미 사진틀에 있는 경우
    if person[i] in p:
        for k in range(len(p)):
            if person[i] == p[k]:
                vote[k] += 1
                break
    # 사진틀에 없는 경우
    else:
        # 사진틀이 꽉차서 새로 등록
        if len(p) == n:
            for k in range(n):
                # 투표수가 작은 사람 지우기
                m = min(vote)
                if vote[k] == m:
                    del p[k]
                    del vote[k]
                    break
        # 사진틀이 1개이상 비어있음 -> 새로 등록하기
        p.append(person[i])
        vote.append(1)
p.sort()
print(' '.join(map(str,p)))
