from _collections import deque
for tc in range(1,11):
    n = int(input())
    password = deque(list(map(int,input().split())))
    i = 1
    while True:
        first = password.popleft()
        first -= i
        if first <0 :
            first = 0
        password.append(first)
        if first == 0:
            break
        i += 1
        if i == 6:
            i = 1
    res = list(password)
    res = (list(map(str,res)))
    res = ' '.join(res)

    print("#{} {}".format(tc,res))