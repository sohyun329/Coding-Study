from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    time = 0
    cur_weight = 0 # 현재 다리 위 무게
    
    while truck_weights:
        cur_weight -= bridge.popleft() # 다리 위로 트럭 하나 건너기 시작할 때 bridge 칸 하나 삭제
        time += 1
        
        # 현재 다리 위 weight
        if cur_weight + truck_weights[0] <= weight :
            cur_weight += truck_weights[0] # 현재 다리 위 무게 
            bridge.append(truck_weights.popleft()) # bridge에 현재 다리 위 올라가 있는 truck 값 저장
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))