def solution(places):
    answer = []
    for place in places:
        case = []
        for i in range(5):
            place[i] = list(place[i])
            for j in range(5):
                if place[i][j] == 'P':
                    case.append([i,j])
        flag = True
        for i in range(len(case)):
            x, y = case[i]
            # 왼쪽
            for j in range(y-1,y-3,-1):
                if 0 <= j < 5:
                    if place[x][j] == 'P':
                        flag = False
                        break
                    if place[x][j] == 'X':
                        break
            #오른쪽
            for j in range(y+1,y+3):
                if 0 <= j < 5:
                    if place[x][j] == 'P':
                        flag = False
                        break
                    if place[x][j] == 'X':
                        break
            #위쪽
            for j in range(x-1,x-3,-1):
                if 0 <= j < 5:
                    if place[j][y] == 'P':
                        flag = False
                        break
                    if place[j][y] == 'X':
                        break
            #아래쪽
            for j in range(x+1,x+3):
                if 0 <= j < 5:
                    if place[j][y] == 'P':
                        flag = False
                        break
                    if place[j][y] == 'X':
                        break
            # 오른쪽 아래 대각선
            if 0 <= x < 4 and 0 <= y < 4:
                if place[x+1][y+1] == 'P':
                    if place[x+1][y] == 'X' and place[x][y+1] == 'X':
                        pass
                    else:
                        flag = False
            # 왼쪽 아래 대각선
            if 0 <= x < 4 and 0 < y < 5:
                if place[x+1][y-1] == 'P':
                    if place[x+1][y] == 'X' and place[x][y-1] == 'X':
                        pass
                    else:
                        flag = False
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer