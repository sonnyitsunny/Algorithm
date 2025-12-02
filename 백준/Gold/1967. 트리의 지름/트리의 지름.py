import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
graph=[[]for _ in range(n+1)]

for _ in range(n-1):
    p,c,d=map(int,input().split())
    graph[p].append((c,d))
    graph[c].append((p,d))

def bfs(start):
    
    q=deque()
    visited=[-1]*(n+1)
    visited[start]=0
    q.append((start))


    while q:
        now=q.popleft()
            
        for nxt,dist in graph[now]: #연결되어있고
            if visited[nxt]==-1: #방문하지 않은 곳이라면
                visited[nxt]=visited[now]+dist
                q.append(nxt)

    far_node=visited.index(max(visited))
    far_dist=max(visited)
    return far_node,far_dist
        
A,_=bfs(1)
_,diameter=(bfs(A))

print(diameter)