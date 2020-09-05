for tc in range(1,11):
    n = int(input())
    num_list = list(map(int,input().split()))
    cnt = 0
    for i in range(2,n-1):
        if num_list[i] > num_list[i-2] and num_list[i] > num_list[i-1] and num_list[i] > num_list[i+1] and num_list[i] > num_list[i+2]:
            a = max(num_list[i-1],num_list[i-2],num_list[i+1],num_list[i+2])
            cnt += (num_list[i] - a)

    print("#{} {}".format(tc,cnt))
