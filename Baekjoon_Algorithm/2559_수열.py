import sys
def tow_pointer(arr,n,k):
    start, end = 0, k
    res = sum(arr[start:end])
    s = res
    while end < n:
        s = s + arr[end] - arr[start]
        start += 1
        end += 1
        res = max(res, s)
    return res
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = tow_pointer(arr,n,k)
print(res)