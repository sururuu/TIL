t=int(input())
for tc in range(1,t+1):
    n,m,l=map(int,input().split())
    num=list(input().split())
    for i in range(m):
        index,number = map(int,input().split())
        num1=num[:index]
        num1.append(number)
        num2=num[index:]
        num3 = num1+num2
        num=num3
    res=int(num[l])
    print("#{} {}".format(tc,res))