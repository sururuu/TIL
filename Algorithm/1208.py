def sort_number(number_list,number):
    for j in range(number):
        for i in range(number- 1):
            if number_lists[i] > number_lists[i + 1]:
                number_lists[i], number_lists[i + 1] = number_lists[i + 1], number_lists[i]


for i in range(10):
    number = int(input())
    number_lists = list(map(int, input().split()))
    sort_number(number_lists,len(number_lists))

    for k in range(number):
        number_lists[-1], number_lists[0] = number_lists[-1] - 1, number_lists[0] + 1
        sort_number(number_lists,len(number_lists))
        final_number = number_lists[-1] - number_lists[0]
        if number_lists[-1] - number_lists[0] <= 1:
            break
    print(f"#{i + 1} {final_number}")