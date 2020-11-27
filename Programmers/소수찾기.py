from itertools import permutations

def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(x**(0.5))+1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(map(int,numbers))
    result_list = []
    for i in range(1,len(numbers)+1):
        new_list = (list(permutations(numbers,i)))
        for j in range(len(new_list)):
            new_number = ''
            for k in range(i):
                if new_list[j][0] != 0:
                    new_number += str(new_list[j][k])
            if len(new_number) >0 :
                if int(new_number) not in result_list and is_prime(int(new_number)):
                    print(result_list)
                    result_list.append(int(new_number))
                    answer += 1



    return answer

