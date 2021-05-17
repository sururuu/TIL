prime = [1] * 100001
for i in range(2,int(100001**(0.5))+1):
    for j in range(i+i,100001,i):
        prime[j] = 0
t = int(input())
for tc in range(t):
    n = int(input())
    cnt = {}
    for i in range(2,n+1):
        if prime[i]:
            while True:
                if n % i == 0:
                    n //= i
                    if i not in cnt:
                        cnt[i] = 1
                    else:
                        cnt[i] += 1
                else:
                    break
    for key,value in cnt.items():
        print(key,value)
