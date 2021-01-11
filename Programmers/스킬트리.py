def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for skill_tree in skill_trees:
        tree = list(skill_tree)
        index = []
        while tree:
            word = tree.pop(0)
            if word in skill:
                index.append(word)
        if len(skill) == len(index):
            if skill == index:
                answer += 1
        else:
            l = len(index)
            if skill[:l] == index:
                answer += 1
    return answer