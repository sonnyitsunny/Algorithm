from collections import defaultdict
def solution(nums):
    answer = 0
    poc=defaultdict(int)
    n=len(nums)/2
    
    
    for i in nums:
        if i in poc:
            pass
        else:
            poc[i]=1
    
    m=len(poc.keys())
    if m>=n:
        answer=n
    else:
        answer=m
    
    
    
    
    return answer