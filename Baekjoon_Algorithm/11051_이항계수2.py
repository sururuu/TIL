import math
n,k = map(int,input().split())
# nCk -> n!/(k!(n-k)!)
res = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
print(res%10007)