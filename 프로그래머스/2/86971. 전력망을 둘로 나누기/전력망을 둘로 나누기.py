from collections import deque

def solution(n, wires):
    answer=n
    graph=[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    
    def bfs(start):
        q=deque()
        q.append(start)
        visited=[False]*(n+1)
        visited[start]=True
        cnt=1
        while q:
            t=q.popleft()
            
            for next in graph[t]:
                if not visited[next]:
                    visited[next]=True
                    q.append(next)
                    cnt+=1
        return cnt
    
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer=min(abs(bfs(a)-bfs(b)),answer)
        
        
        graph[a].append(b)
        graph[b].append(a)
    
    
    
    
    return answer