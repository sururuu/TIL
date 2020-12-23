N = int(input())
candy = [list(input()) for _ in range(N)]
res = 0
def garo():
    global res
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
            else:
                if res < cnt:
                    res = cnt
                cnt = 1
        if res < cnt:
            res = cnt

def sero():
    global res
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1
            else:
                if res < cnt:
                    res = cnt
                cnt = 1
        if res < cnt:
            res = cnt
#가로
for i in range(N):
    for j in range(N-1):
        # 인접한 수가 다르면 바꾸기
        # 가로줄 세로줄 각각 연속된 문자 갯수 구하기
        # 바꾼 두수 다시 돌려놓기
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            garo()
            sero()
            candy[i][j], candy[i][j + 1] = candy[i][j+1], candy[i][j]
#세로
for i in range(N):
    for j in range(N-1):
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            garo()
            sero()
            candy[j][i], candy[j+1][i] =  candy[j+1][i], candy[j][i]
# 갯수 세기
print(res)