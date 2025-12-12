from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge=deque([0]*bridge_length)
    trucks=deque(truck_weights)
    cur_weight = 0
    while bridge:
        
        answer+=1
        cur_weight-=bridge.popleft()
        
        if trucks:
            if cur_weight+trucks[0]<=weight:
                t_we=trucks.popleft()
                bridge.append(t_we)
                cur_weight+=t_we
            else:
                bridge.append(0)
        
    
    
    
    return answer