def solution(n):
    answer = 0
    ans = ''
    while n:
        n, r = divmod(n, 3)
        ans += str(r)
    number = list(map(int,ans))
    for idx, num in enumerate(number):
        answer += 3**(len(number)-idx-1)*num
    return answer
def solution2(n):
    answer = 0
    tmp = ''
    while n:
        n,r = divmod(n, 3)
        tmp += str(r)
    # 3진수 스트링을 10진수로 변환
    answer = int(tmp, 3)
    return answer
