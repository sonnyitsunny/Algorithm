from math import lcm
def solution(signals):
    
    limit=1
    
    for sign in signals:
        limit=lcm(sum(sign),limit)
        
    for time in range(1,limit+1):
        check=True
        for sign in signals:
            g,y,r=sign
            cycle=g+y+r
            pos=time%cycle
            
            if g+1<=pos<=g+y:
                continue
            else:
                check=False
                break
        if check:
            return time
    return -1