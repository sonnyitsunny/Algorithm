def solution(elements):
    answer = 0
    res=set()
    
    n=len(elements)
    
    elements=elements+elements[:n-1]
    
    for i in range(1,n+1):
        for j in range(n):
            if j<n:
                res.add(sum(elements[j:j+i]))
    
    answer=len(res)
    return answer