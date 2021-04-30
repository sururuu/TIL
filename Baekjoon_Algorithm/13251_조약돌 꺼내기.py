M = int(input())
stone_arr = list(map(int,input().split()))
K = int(input())
ans = 0
S = sum(stone_arr)
for stone in stone_arr:
    if stone >= K:
        n = 1
        for i in range(K):
            n *= (stone-i)
            n /= (S-i)
        ans += n
print(ans)

# nCr 조합 -> 런타임 에러 (OverflowError)
# 각각의 확률을 구해서 해결!