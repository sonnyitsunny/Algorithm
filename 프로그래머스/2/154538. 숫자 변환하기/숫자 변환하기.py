from collections import deque
def solution(x, y, n):
    
    visited=set()
    
    q=deque()
    q.append((x,0))
    visited.add(x)
    
    while q:
        target,cnt=q.popleft()
        
        if target==y:
            return cnt
        
        for nxt in (target*3,target*2,target+n):
            if nxt not in visited and nxt<=y:
                visited.add(nxt)
                q.append((nxt,cnt+1))
    
    
    return -1