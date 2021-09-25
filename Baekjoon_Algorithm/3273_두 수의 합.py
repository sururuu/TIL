import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
res = 0
arr.sort()
left, right = 0, n-1
while left < right:
    target = arr[left] + arr[right]
    if target == k:
        res += 1
    if target > k:
        right -= 1
    else:
        left += 1
print(res)

# 투 포인터!