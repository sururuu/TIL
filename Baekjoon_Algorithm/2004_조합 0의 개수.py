def sol(n,k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

n,m = map(int,input().split())
# 끝자리가 0의 개수 -> 10의 배수 찾기
# 10 = 2 * 5
five_cnt = sol(n,5) - sol(m,5) - sol(n-m,5)
two_cnt = sol(n,2) - sol(m,2) - sol(n-m,2)
ans = min(five_cnt,two_cnt)
print(ans)