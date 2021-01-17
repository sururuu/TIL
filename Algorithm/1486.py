from itertools import combinations
t = int(input())
for tc in range(1,t+1):
    N,B = map(int,input().split())
    heigt = list(map(int,input().split()))
    sub_list =[]
    for i in range(1,N+1):
        sub_list.append((list(combinations(heigt,i))))
    sum_list =[]
    for i in range(N):
        for j in range(len(sub_list[i])):
            if sum(sub_list[i][j]) >= B:
                sum_list.append(abs(B-sum(sub_list[i][j])))
    print("#{} {}".format(tc,min(sum_list)))

