def isPrime(number):
    if number < 2:
        False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num*10 + i
            if isPrime(temp):
                dfs(temp)
n = int(input())
for i in [2,3,5,7]:
    dfs(i)