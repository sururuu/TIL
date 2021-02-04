def Binary(arr,target,low,high):
    if low > high:
        return False
    mid = (low+high)//2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        low = mid+1
        return Binary(arr,target,low,high)
    elif arr[mid] > target:
        high = mid-1
        return Binary(arr,target,low,high)

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

for num in m_list:
    if Binary(n_list,num,0,n-1):
        print(1)
    else:
        print(0)