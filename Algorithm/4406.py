t = int(input())
for tc in range(1,t+1):
    exclude = ['a','e','i','o','u']
    case = list(map(str,input()))
    after = []
    for i in range(len(case)):
        if case[i] not in exclude:
            after.append(case[i])
    after = ''.join(after)
    print("#{} {}".format(tc,after))