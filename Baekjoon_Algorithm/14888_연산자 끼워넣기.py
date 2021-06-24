from itertools import permutations
n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
case = ['+', '-', '*', '//']
cal = []
for i in range(4):
    for j in range(arr2[i]):
        cal.append(case[i])
minRes = 10**9
maxRes = -10**9
case2 = list(set(list(permutations(cal, n-1))))
for target in case2:
    num = arr[0]
    for i in range(n-1):
        if target[i] == '+':
            num += arr[i+1]
        elif target[i] == '-':
            num -= arr[i+1]
        elif target[i] == '*':
            num *= arr[i+1]
        else:
            if num < 0:
                s = abs(num) // arr[i+1]
                num = -s
            else:
                num //= arr[i+1]
    minRes = min(minRes,num)
    maxRes = max(maxRes,num)
print(maxRes)
print(minRes)