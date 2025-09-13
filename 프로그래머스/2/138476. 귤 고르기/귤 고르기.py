from collections import Counter
def solution(k, tangerine):
    answer = 0
    d=Counter(tangerine)
    
    d_sort=sorted(d.items(),key=lambda x: -x[1])
    
    for i in d_sort:
        k-=i[1]
        
        answer+=1
        if k<=0:
            break
    
    
    return answer