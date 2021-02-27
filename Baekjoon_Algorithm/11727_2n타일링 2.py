n = int(input())
case = [1,3]
for i in range(n):
    num = case[-1] + case[-2] * 2
    case.append(num)
print(case[n-1]%10007)