import copy
t = int(input())
for tc in range(1,t+1):
    text = input()
    text = list(text)
    result = []
    result = copy.deepcopy(text)
    result = list(set(result))
    result.sort()
    res2 = ''
    for i in range(len(result)):
        if text.count(result[i]) % 2 == 1:
            res2 += result[i]
    res = 'Good'
    if len(res2) == 0:
        print("#{} {}".format(tc,res))
    else:
        print("#{} {}".format(tc,res2))