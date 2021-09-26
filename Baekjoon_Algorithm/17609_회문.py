def confirm(s, start, end):
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
t = int(input())
for tc in range(t):
    s = input()
    res = 0
    flag = True
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            res = 1
            left = confirm(s, start+1, end)
            right = confirm(s, start, end-1)
            if left or right:
                res = 1
            else:
                res = 2
            break
    print(res)

