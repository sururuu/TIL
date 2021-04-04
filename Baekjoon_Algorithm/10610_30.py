n = int(input())
num = list(map(int,str(n)))
if 0 not in num:
    print(-1)
    exit()
if sum(num) % 3 != 0:
    print(-1)
    exit()
num = sorted(num,reverse=True)
num = list(map(str,num))
print(''.join((num)))