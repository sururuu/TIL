def change(word):
    m = word.replace("D#","d").replace("C#","c").replace("F#","f").replace("A#","a").replace("G#","g")
    return m

def solution(m, musicinfos):
    answer = set()
    m = change(m)
    for idx,mus in enumerate(musicinfos):
        s,e,name,melody = mus.split(",")
        s = list(map(int,s.split(":")))
        e = list(map(int,e.split(":")))
        time = (e[0]*60+e[1]) - (s[0]*60+s[1])
        melody = change(melody)
        melody = (melody*time)[:time]
        if m in melody:
            answer.add((idx,name,time))
    answer = list(answer)
    # 시간순 -> idx 기준으로 정렬
    answer = sorted(answer,key=lambda x:(-x[2], x[0]))
    if len(answer) == 0:
        answer = "(None)"
    else:
        answer = answer[0][1]
    return answer