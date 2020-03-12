t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=[[0]*n for i in range(n)]
    cnt=1
    row_start=0
    col_start=0
    row_end=n-1
    col_end=n-1
    while row_start<=row_end and col_start<=col_end:
        #왼쪽 -> 오른쪽
        for i in range(col_start,col_end+1):
            arr[row_start][i]=cnt
            cnt+=1
        row_start+=1

        #위 -> 아래
        for i in range(row_start,row_end+1):
            arr[i][col_end]=cnt
            cnt+=1
        col_end-=1

        #오른쪽 -> 왼쪽
        for i in range(col_end,col_start-1,-1):
            arr[row_end][i]=cnt
            cnt+=1
        row_end-=1

        #아래 -> 위
        for i in range(row_end,row_start-1,-1):
            arr[i][col_start]=cnt
            cnt+=1
        col_start+=1
    print("#{}".format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
        
 #예시출력
    '''#1
    1 2 3
    8 9 4
    7 6 5
    #2
    1 2 3 4
    12 13 14 5
    11 16 15 6
    10 9 8 7'''
