def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    cur=targets[0][1]
    answer=1
    
    for s,e in targets[1:]:
        if s<cur:
            continue
        else:
            answer+=1
            cur=e
                
    
    
    
    
    
    
    return answer