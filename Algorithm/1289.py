t = int(input())
for tc in range(1,t+1):
    memory = list(input())
    zero = '0'
    cnt = 0
    for i in range(len(memory)):
        if memory[i] != zero:
           cnt += 1
           zero = memory[i]
        else:
            pass
    print("#{} {}".format(tc,cnt))