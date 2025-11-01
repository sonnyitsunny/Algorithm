import heapq

def solution(n, k, enemy):
    answer = 0
    combat=[]
    
    
    for e in enemy:
        n-=e
        heapq.heappush(combat,-e)
        
        if n<0:
            if k>0:
                n+=-heapq.heappop(combat)
                k-=1
                answer+=1
                
            else:
                break
        else:
            answer+=1
                
    return answer