def check(s):
    stack = []
    if len(s) % 2 == 1:
        return False
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == ']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        return False
    else:
        return True
def cal(s):
    res = 0
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')' and stack:
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k] == '(':
                        stack[-1] = temp * 2
                        break
                    else:
                        temp += stack[k]
                        stack.pop()
        elif s[i] == ']' and stack:
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k] == '[':
                        stack[-1] = temp * 3
                        break
                    else:
                        temp += stack[k]
                        stack.pop()
    res = sum(stack)
    return res

s = list(input())
if check(s):
    print(cal(s))
else:
    print(0)
