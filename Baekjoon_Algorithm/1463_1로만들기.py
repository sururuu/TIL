n = int(input())
cnt = 0
count = set([n])
while True:
    case = set()
    if 1 in count:
        break
    for value in count:
        if value % 3 == 0:
            case.add(value//3)
        if value % 2 == 0:
            case.add(value//2)
        case.add(value-1)
    count = count.union(case)
    cnt += 1
print(cnt)