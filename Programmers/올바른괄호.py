def solution(s):
    stack = []
    for target in s:
        if target == '(':
            stack.append(target)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True if len(stack) == 0 else False