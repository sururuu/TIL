cost=list(map(int,input().split()))
table=list(map(int,input().split()))

def f(n,s,d,m,m3):
    global minV
    if n>12:
        if minV > s:
            minV = s
            return minV
    else:
        f(n+1,s+min(table[n]*d,m),d,m,m3) #1일 1달 비교
        f(n+3,s+m3,d,m,m3) #3달이용권

f(12,cost[-1],sum(table),len(table),len(table))