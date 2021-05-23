n = int(input())
# n이 5미만인 경우 자기자신이 가장 큰수가 됨
# n이 5이상인 경우 3으로 분해하기
if n < 5:
    print(n)
else:
    res = 1
    while n >= 5:
        res *= 3
        res %= 10007
        n -= 3
    res *= n
    print(res % 10007)