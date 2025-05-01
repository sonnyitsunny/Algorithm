from collections import defaultdict

def solution(clothes):
    
    hash=defaultdict(int)
    
    for item,name in clothes:
        if name in hash:
            hash[name]+=1
        else:
            hash[name]=1
    
    answer = 1
    for cnt in hash.values():
        answer*=(cnt+1)
    
    return answer-1