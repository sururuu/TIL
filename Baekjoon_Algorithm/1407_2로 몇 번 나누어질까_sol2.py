arr = [0, 1, 3, 4]
def solve(n):
    if n == 0:
        return 0
    q,r = divmod(n,4)
    k = 4*q
    s = k + arr[r] + 4*solve(k//4)
    return s
a, b = map(int,input().split())
res = solve(b) - solve(a-1)
print(res)