from collections import deque
arr = list(input())
stack = deque()
l = len(arr)
cnt = 0
while cnt < l:
    if arr[cnt] == 'P':
        ss = len(stack)
        if ss >=3:
            if stack[-3] == 'P' and stack[-2] == 'P' and stack[-1] == 'A':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('P')
            else:
                stack.append('P')
        else:
            stack.append('P')
    else:
        stack.append('A')

    cnt += 1

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')