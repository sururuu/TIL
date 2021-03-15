n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
m_list = list(map(int,input().split()))
for i in range(m):
    num = m_list[i]
    left,right,flag = 0,n-1,0
    while left <= right:
        m = (left+right)//2
        if card[m] == num:
            flag = 1
            break
        elif card[m] < num:
            left = m + 1
        elif card[m] > num:
            right = m -1
    print(flag,end=" ")
