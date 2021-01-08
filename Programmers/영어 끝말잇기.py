def solution(n, words):
    answer = []
    people = [[] for _ in range(n)]

    for i in range(len(words)):
        idx = i % n
        people[idx].append(words[i])
        if words[i] in words[:i]:
            return [idx + 1, len(people[idx])]
        if 0 < i:
            front = words[i - 1]
            ing = words[i]
            if front[-1] != ing[0]:
                return [idx + 1, len(people[idx])]

    return [0, 0]