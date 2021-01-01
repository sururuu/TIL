from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append((begin,0))
    while q:
        begin,cnt = q.popleft()
        if begin == target:
            return cnt
        cnt += 1
        for word in words:
            count = 0
            for i in range(len(begin)):
                if word[i] != begin[i]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                q.append((word,cnt))
                words.remove(word)
    return answer