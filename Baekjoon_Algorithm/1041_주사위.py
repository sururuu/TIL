n = int(input())
numbers = list(map(int,input().split()))
# 주사위가 1개인 경우
if n == 1:
    print(sum(numbers)-max(numbers))
# 주사위 갯수가 2개 이상인 경우
else:
    edge3 = 4
    edge2 = 4*(n-1) + 4*(n-2)
    other = n**2*5-(edge2*2+edge3*3)
    res = 0

    sumList = []
    sumList.append(min(numbers[0],numbers[5]))
    sumList.append(min(numbers[1],numbers[4]))
    sumList.append(min(numbers[2],numbers[3]))
    sumList.sort()

    res += edge3*sum(sumList)
    res += edge2*sum(sumList[:2])
    res += other*sumList[0]
    
    print(res)