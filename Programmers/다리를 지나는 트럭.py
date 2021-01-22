from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    while bridge:
        answer += 1
        bridge.pop()
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.insert(0,truck_weights.pop(0))
            else:
                bridge.insert(0,0)
    return answer