def solution2(n,a,b):
    answer = 0
    while a != b:
        a = (a+1) >> 1
        b = (b+1) >> 1
        answer += 1
    return answer

def solution1(n,A,B):
    answer = []
    arr = [_ for _ in range(1,n+1)]
    flag = True
    while flag:
        new = []
        for i in range(0,len(arr),2):
            a = arr[i]
            b = arr[i+1]
            if a == A and b == B:
                flag = False
                break
            if a == B and b == A:
                flag = False
                break
            if a == A or b == A:
                new.append(A)
            elif a == B or b == B:
                new.append(B)
            else:
                new.append(a)
        answer.append(new)
        arr = new


    return len(answer)