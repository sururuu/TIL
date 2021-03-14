idx = 123456*2 + 1
arr = [True for _ in range(idx)]
def isPrime():
    m = int(idx**(0.5))+1
    for i in range(2,m):
        if arr[i]:
            for j in range(i+i,idx,i):
                arr[j] = False

isPrime()
n = int(input())
while True:
    cnt = 0
    for i in range(n+1,2*n+1):
        if arr[i]:
            cnt += 1
    print(cnt)
    n = int(input())
    if n == 0:
        break
