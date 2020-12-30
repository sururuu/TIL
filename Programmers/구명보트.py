def solution(people, limit):
    answer = 0
    people.sort()
    for i in range(len(people)):
        if people[i] >= limit:
            answer += (len(people)-i)
            people = people[:i]
            break
    first,end = 0,len(people)-1
    double = 0
    while first<end:
        if people[first] + people[end] <= limit:
            first += 1
            end -= 1
            double += 1
        else:
            end -= 1
    answer += (len(people)-double)
    return answer