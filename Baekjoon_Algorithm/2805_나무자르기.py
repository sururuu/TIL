n,m = map(int,input().split())
tree = list(map(int,input().split()))
left, right = 1, max(tree)
res = 0
while left <= right:
    mid = (left + right) // 2
    height = 0
    for i in range(n):
        if mid < tree[i]:
            height += (tree[i] - mid)
    if height >= m:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)