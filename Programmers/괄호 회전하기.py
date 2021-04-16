def solution(s):
    match_dict = {'}': '{', ')': '(',']': '['}
    answer = 0
    arr = []
    l = len(s)
    while l:
        flag = True
        for target in s:
            if target == '(' or target == '{' or target == '[':
                arr.append(target)
            elif target == ')' or target == '}' or target == ']':
                if len(arr) == 0 or arr[-1] != match_dict[target]:
                    flag = False
                    break
                arr.pop()
        if len(arr) != 0 or flag == False:
            pass
        else:
            answer += 1
        l -= 1
        s = s[1:] + s[0]
    return answer