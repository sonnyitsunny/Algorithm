def solution(sequence, k):
    
    
    n=len(sequence)
    answer = [0,n-1]
    start=0
    res=0
    
    for end in range(n):
        res+=sequence[end]
        
        
        while res>k:
            res-=sequence[start]
            start+=1
        if res==k:
            if end-start<answer[1]-answer[0]:
                answer=[start,end]
    
    
    
    return answer
    