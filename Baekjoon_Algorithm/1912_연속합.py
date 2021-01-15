n = int(input())
numbers = list(map(int,input().split()))
vs = [numbers[0]]
for i in range(len(numbers)-1):
    vs.append(max((vs[i]+numbers[i+1]),numbers[i+1]))
print(max(vs))