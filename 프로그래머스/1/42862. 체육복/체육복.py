def solution(n, lost, reserve):
    

    
    a_lost=list(set(lost)-set(reserve))
    a_reserve=list(set(reserve)-set(lost))
    
    a_lost.sort()
    a_reserve.sort()
    answer = n-len(a_lost)
    for i in a_lost:
        if i in a_reserve:
            answer+=1
            a_reserve.remove(i)
        else:
            a=i-1
            b=i+1

            safe=False

            if a in a_reserve:
                answer+=1
                a_reserve.remove(a)
                safe=True
            if (safe==False) and (b in a_reserve):
                answer+=1
                a_reserve.remove(b)
        
    return answer