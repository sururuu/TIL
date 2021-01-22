from itertools import combinations
l,c = map(int,input().split())
words = list(map(str,input().split()))
vowels = ['a','e','i','o','u']
vowel = []
consonant = []
words.sort()
cases = list(combinations(words,l))
for case in cases:
    cnt1 = 0
    cnt2 = 0
    for i in range(len(case)):
        if case[i] in vowels:
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        print(''.join(case))