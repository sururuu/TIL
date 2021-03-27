def solution(arr):
    answer = [0,0]
    def check(x,y,n):
        target = arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if target != arr[i][j]:
                    m = n//2
                    # 왼쪽 위
                    check(x,y,m)
                    # 오른쪽 위
                    check(x+m,y,m)
                    # 왼쪽 아래
                    check(x,y+m,m)
                    # 오른쪽 아래
                    check(x+m,y+m,m)
                    return
        answer[target] += 1
    check(0,0,len(arr))
    return answer