n = int(input())
n_list = []
while n!= 0:
    n_list.append(n)
    n = int(input())
number = max(n_list)

# 소수인지 아닌지 판별하는 함수
# 에라토스테네스의 체
arr = [True for _ in range(number)]
def isPrime():
    m = int(number**(0.5))
    for i in range(2,m+1):
        if arr[i]:
            for j in range(i+i,number,i):
                arr[j] = False

isPrime()
for n in n_list:
    for i in range(3,n-1,2):
        if arr[i] and arr[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break
