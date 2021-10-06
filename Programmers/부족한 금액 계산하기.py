def solution(price, money, count):
    answer = 0
    num = 0
    for i in range(1,count+1):
        num += price * i
    if num <= money:
        answer = 0
    else:
        answer = num - money

    return answer