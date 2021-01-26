def solution(number, k):
    answer = []
    number = list(number)
    answer.append(number[0])
    for num in number[1:]:
        while len(answer) > 0 and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()

        answer.append(num)

    # k가 남았을 경우 뒷자리 k개 버림
    if k != 0:
        answer = answer[:-k]
    answer = ''.join(answer)
    return answer
