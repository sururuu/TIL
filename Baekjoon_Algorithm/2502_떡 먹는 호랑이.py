def count(n):
    arr = [0,1]
    if n == 0:
        return arr[0]
    elif n == 1:
        return arr[1]
    else:
        return count(n-1)+count(n-2)

day, cnt = map(int,input().split())
n1 = count(day - 2)
n2 = count(day - 1)
for i in range(1,cnt):
    for j in range(i,cnt):
        if day == 3:
            if i + j == cnt:
                print(i,j,sep='\n')
                exit()
        else:
            if n1*i + n2*j == cnt:
                print(i,j,sep='\n')
                exit()