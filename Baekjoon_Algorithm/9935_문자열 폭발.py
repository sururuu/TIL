s = list(input())
target = list(input())
stack = []
l = len(target)
for i in range(len(s)):
    stack.append(s[i])
    if s[i] == target[-1]:
        m = len(stack)
        if stack[-l:] == target:
            del stack[-l:]
if stack:
    print(''.join(stack))
else:
    print("FRULA")