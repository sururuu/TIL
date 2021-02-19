t=int(input())
for tc in range(1,t+1):
    s=input()
    n=len(s)
    i=0
    res=''
    if n==1:
        res='exist'
    else:

        while i<n//2 and ((s[i]==s[-i-1]) or(s[i]=='?') or ('?'==s[-i-1])):
            i+=1
        if i==n//2:
            res=('exist')
        else:
            res=('Not exist')
    print("#{} {}".format(tc,res))