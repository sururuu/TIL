for tc in range(1,11):
    n = int(input())
    word = list(input())
    sentence = list(input())
    length = len(word)
    sentenceLength = len(sentence)
    res = 0
    first = word[0]
    for i in range(sentenceLength-length+1):
        if first == sentence[i]:
            if word == sentence[i:i+length]:
                res += 1
    print("#{} {}".format(tc,res))