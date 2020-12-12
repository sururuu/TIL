def multy(n,m):
    if m > 1:
        return n*multy(n,m-1)
    else:
        return n

for tc in range(1,11):
    t = int(input())
    n,m = map(int,input().split())
    res = (multy(n,m))
    print("#{} {}".format(tc,res))