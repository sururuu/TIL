n, k = map(int,input().split())
arr = list(map(int,input().split()))
start = 0
res = 0
case = [0] * (max(arr)+1)
for i in range(n):
    num = arr[i]
    case[num] += 1
    if case[num] > k:
        res = max(res, i-start)
        while case[num] > k:
            case[arr[start]] -= 1
            start += 1
    else:
        res = max(res,i-start+1)
print(res)