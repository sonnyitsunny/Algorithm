import math
def solution(n, k):
    answer = []
    people=[i for i in range(1,n+1)]
    
    k-=1
    
    for i in range(n,0,-1):
        fact=math.factorial(i-1)
        idx=k//fact
        k=k%fact
        
        answer.append(people.pop(idx))
    
    
    
    
    return answer