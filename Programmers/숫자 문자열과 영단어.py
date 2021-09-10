from collections import deque

change = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
          'eight': '8', 'nine': '9'}


def solution(s):
    answer = s
    for idx, item in change.items():
        answer = answer.replace(idx, item)
    return int(answer)


def solution2(s):
    answer = 0
    temp = []
    q = deque(list(s))

    while q:
        target = q.popleft()
        if target.isdigit():
            temp.append(target)
        else:
            tem = target
            while True:
                if q:
                    next_target = q.popleft()
                    if next_target.isdigit():
                        q.appendleft(next_target)
                        break
                    else:
                        tem += next_target
                        if tem in change:
                            temp.append(change[tem])
                            break

                else:
                    break

    return int(''.join(temp))