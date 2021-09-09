def str_to_int(time):
    h,m,s = time.split(':')
    return int(h)*3600+int(m)*60+int(s)

def int_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str(time % 3600 // 60).zfill(2)
    s = str(time % 3600 % 60).zfill(2)
    return h+':'+m+':'+s

def solution(play_time, adv_time, logs):
    answer = 0
    if play_time == adv_time:
        return "00:00:00"
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    state = [0] * (play_time+1)
    for log in logs:
        start, end = log.split("-")
        start, end = str_to_int(start), str_to_int(end)
        state[start] += 1
        state[end] -= 1
    for i in range(1,len(state)):
        state[i] += state[i-1]
    for i in range(1,len(state)):
        state[i] += state[i-1]
    max_time = state[adv_time-1]
    for i in range(adv_time,play_time):
        if state[i] - state[i-adv_time] > max_time:
            max_time = state[i] - state[i-adv_time]
            answer = i-adv_time+1

    return int_to_str(answer)