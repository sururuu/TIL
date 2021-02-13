n_list = [int(input()) for _ in range(n)]
# number = max(n_list)
# 소수인지 아닌지 판별하는 함수
# 에라토스테네스의 체
arr = [True for _ in range(10001)]
def isPrime():
    m = int(10001**(0.5))
    for i in range(2,m+1):
        if arr[i]:
            for j in range(i+i,10001,i):
                arr[j] = False
isPrime()
n = int(input())
for n in n_list:
    m = n // 2
    for i in range(m,1,-1):
        if arr[n-i] and arr[i]:
            print(i,n-i)
            break

