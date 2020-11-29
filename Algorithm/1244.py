def dfs(arr,cnt,value):
    global  res,numbers_sort
    if cnt == n:
        if res <value:
            res = value
            return
        else:
            return
    if value == numbers_sort and (n-cnt)%2 == 0:
        res = ''.join(map(str,numbers_sort))
        cnt = 0
        return
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            new = arr[:]
            new[i], new[j] = new[j], new[i]
            new_value = int(''.join(new))
            if new_value not in dist[cnt]:
                dfs(new,cnt+1,new_value)
                dist[cnt].append(new_value)
t = int(input())
for tc in range(1,t+1):
    num , n = input().split()
    n= int(n)
    numbers = list(num)
    numbers_sort = sorted(numbers,reverse= True)
    dist = {i: [] for i in range(n)}
    #print(dist)
    res = 0
    #print(num_str)
    dfs(numbers,0,num)


    print("#{} {}".format(tc,res))