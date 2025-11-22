from collections import Counter
def solution(weights):
    answer = 0
    counter=Counter(weights)
    
    for w in counter:
        if counter[w]>=2:
            answer+=(counter[w]*(counter[w]-1))//2
    
    for w in counter:
        t1 = (w * 3) / 2
        t2= w * 2
        
        t3 = (w * 4) / 3
        if t1 in counter:
            answer+=counter[w]*counter[t1]
        if t2 in counter:
            answer+=counter[t2]*counter[w]
        if t3 in counter:
            answer+=counter[w]*counter[t3]
    
    return answer