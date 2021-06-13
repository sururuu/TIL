def solution(N, number):
    answer = 0
    if N == number:
        return 1
    s = [set() for _ in range(8)]
    for i in range(8):
        s[i].add(int(str(N)*(i+1)))
    for i in range(1,8):
        for j in range(i):
            for oper1 in s[j]:
                for oper2 in s[i-j-1]:
                    s[i].add(oper1+oper2)
                    s[i].add(oper1-oper2)
                    s[i].add(oper1*oper2)
                    if oper2 != 0:
                        s[i].add(oper1//oper2)
        if number in s[i]:
            return i+1
    return -1