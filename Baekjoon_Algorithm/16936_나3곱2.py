from copy import deepcopy
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    res = [arr[i]]
    num = arr[i]
    rest = deepcopy(arr)
    del rest[i]
    while rest:
        if num % 3 == 0 and num // 3 in rest:
            rest.remove(num//3)
            res.append(num//3)
            num = num // 3
        elif num *2 in rest:
            rest.remove(num*2)
            res.append(num*2)
            num = num * 2
        else:
            break
    if rest:
        pass
    else:
        print(*res)
        break