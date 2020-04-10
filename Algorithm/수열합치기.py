t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    first_list = []
    for i in range(m):
        first_list.append(list(input().split()))

    curl_list = first_list[0]

    for i in range(1,m):
        for j in range(len(curl_list)):
            if int(first_list[i][0]) < int(curl_list[j]):
                curl_front = curl_list[:j]
                curl_end = curl_list[j:]
                curl_list = curl_front + first_list[i] + curl_end
                break
        if (i+1)*n != len(curl_list):
            curl_end = curl_list[:]
            curl_list = curl_end + first_list[i]

    res=curl_list[-1:-11:-1]
    print("#{} {}".format(tc,' '.join(res)))
