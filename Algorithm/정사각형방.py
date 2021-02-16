T= int(input())
for tc in range(1,T+1):
    number=int(input())
    num_list = [list(map(int,input().split())) for i in range(number)]

    x=[0,-1,0,1]
    y=[-1,0,1,0]
    max_count=[0]
    count_list=[]
    val_list=[]
    for i in range(number):
        for j in range(number):
            xx=i
            yy=j
            count = 1
            while True:
                check=False
                for k in range(4):
                    text_x=i+x[k]
                    test_y=j+y[k]
                    if 0<=text_x<number and 0<=test_y<number:
                        if num_list[i][j]+1==num_list[text_x][test_y]:
                            count+=1
                            i=text_x
                            j=test_y
                            check=True
                            break
                if not check:
                    break
            if max_count[-1]< count:
                max_count.append(count)
                val_list.append(num_list[xx][yy])
            elif max_count[-1]==count:
                max_count.append((count))
                val_list.append((num_list[xx][yy]))

    max_index=max_count.index(max(max_count))
    result=val_list[max_index-1]
    if max_count.count(max(max_count))>1:
        max_count_ = max_count.count(max(max_count))
        for i in range(max_count_-1):
            max____index=max_index+i
            if result > val_list[max____index]:
                result = val_list[max____index]
    print("#{0} {1} {2} ".format(tc,result,max(max_count)))