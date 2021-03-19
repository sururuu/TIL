target = int(input())
m = int(input())
num = [ _ for _ in range(10)]
if m > 0:
    broken = list(map(int,input().split()))
    for i in range(10):
        if i in broken:
            num.remove(i)
# 숫자를 누를 수 없는 경우
if len(num) == 0:
    print(abs(100-target))
    exit()
# 기본값 시작점 100과 끝점 target 차이로 시작
res = abs(target-100)
# 0부터 비교 -> num에 있는지 확인
# num에 없으면 case에서 제외
# i가 num에 모두 있으면 계산

for i in range(1000001):
    changeArr = list(map(int,str(i)))
    flag = True
    for j in changeArr:
        if j not in num:
            flag = False
            break
    if flag:
        res = min(res,abs(target-i)+len(changeArr))
print(res)
