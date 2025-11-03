
from collections import deque
def solution(priorities, location):
    q=deque()
    for i,p in enumerate(priorities):
        q.append((i,p))
        
    order=0
    while q:
        idx,process=q.popleft()
        found=False
        for _,p in q:
            if process<p:
                found=True
                break
        if found:
            q.append((idx,process))
        else:
            order+=1
            if idx==location:
                return order
    
    
    