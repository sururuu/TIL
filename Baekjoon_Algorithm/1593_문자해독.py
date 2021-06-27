import sys
input = sys.stdin.readline
g, n = map(int,input().split())
W = list(input())
S = list(input())
res = 0
# a ~ z, A ~ Z 52개
w_state = [0] * 52
s_state = [0] * 52
for i in range(g):
    if 'a' <= W[i] <= 'z':
        w_state[ord(W[i]) - ord('a')] += 1
    else:
        w_state[ord(W[i]) - ord('A') + 26] += 1
start, length = 0, 0
for i in range(n):
    if 'a' <= S[i] <= 'z':
        s_state[ord(S[i]) - ord('a')] += 1
    else:
        s_state[ord(S[i]) - ord('A') + 26] += 1
    length += 1
    # 단어 길이가 g 가 되었을 때 비교
    # 비교 후 맨 첫번째 단어 지우고 문장의 첫번째 위치 변경
    # 다음 for 문에서 마지막 단어 삽입하여 다시 비교
    if length == g:
        if w_state == s_state:
            res += 1
        start_word = S[start]
        if 'a' <= start_word <= 'z':
            s_state[ord(start_word) - ord('a')] -= 1
        else:
            s_state[ord(start_word) - ord('A') + 26] -= 1
        start += 1
        length -= 1
print(res)
