def isPrime(num):
    m = int(num**(0.5)) + 1
    if n == 1:
        return False
    for i in range(2,m):
        if num % i == 0:
            return False
    return True
def pelindrom(arr):
    l = len(arr)
    m = l // 2
    if l % 2 == 0:
        right = arr[m:]
    else:
        right = arr[m+1:]
    left = arr[:m]
    right.reverse()
    if left == right:
        return True
    else:
        return False
n = int(input())
while True:
    number = isPrime(n)
    if number:
        arrN = list(map(int,str(n)))
        if pelindrom(arrN):
            print(n)
            break
        else:
            n += 1
    else:
        n += 1