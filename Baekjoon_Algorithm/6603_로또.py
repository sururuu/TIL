from  itertools import combinations
input_list = list(map(int,input().split()))

while True:
    if len(input_list) == 1:
        exit()
    k = input_list[0]
    num_list = input_list[1:]
    case = list(combinations(num_list,6))
    for i in range(len(case)):
        c = list(map(str,case[i]))
        c = ' '.join(c)
        print(c)
    print()
    input_list = list(map(int, input().split()))

