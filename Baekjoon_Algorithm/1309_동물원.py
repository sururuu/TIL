n = int(input())
# [사자없는 경우, 왼쪽에 있는 경우, 오른쪽에 있는 경우 ]
zoo = [[0,0,0] for _ in range(n+1)]
zoo[1] = [1,1,1]
for i in range(2,n+1):
    zoo[i][0] = ( zoo[i-1][0] + zoo[i-1][1] + zoo[i-1][2] ) % 9901
    zoo[i][1] = ( zoo[i-1][0] + zoo[i-1][2] ) % 9901
    zoo[i][2] = ( zoo[i-1][0] + zoo[i-1][1] ) % 9901
print(sum(zoo[-1]) % 9901)