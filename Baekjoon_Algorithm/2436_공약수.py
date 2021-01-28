# 유클리드 호제법
def gcd(a,b):
    while b:
        mod = b
        b = a%b
        a = mod
    return a

G,L = map(int,input().split())
div = L//G
a,b = 1,div
for i in range(1,div//2+1):
    if div % i == 0:
        num1 = i
        num2 = div//i
        # 최대공약수 1인 경우
        if gcd(num1,num2) != 1:
            continue
        if a+b > num1+num2:
            a = num1
            b = num2
print(a*G,b*G)

