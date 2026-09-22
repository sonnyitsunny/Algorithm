def solution(n, lost, reserve):
    answer = 0
    
    both=set(lost)&set(reserve)
    lost=sorted(set(lost)-set(both))
    reserve=sorted(set(reserve)-set(both))
    
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
        elif (r+1) in lost:
            lost.remove(r+1)
    
    answer=n-len(lost)
    
    
    return answer 