import sys
n = int(input())
arr = list(map(int,input().split()))
res = []
m = sys.maxsize
arr.sort()
for i in range(n-2):
    # 세개중 한개를 미리 선택 후 두개 정하기
    first = i
    new_arr = arr[i+1:]
    start, end = i+1, n - 1
    while start < end:
        s = arr[first] + arr[start] + arr[end]
        if abs(s) < m:
            m = abs(s)
            res = [arr[first], arr[start], arr[end]]
        if s < 0:
            start += 1
        elif s > 0:
            end -= 1
        else:
            break
print(*res)