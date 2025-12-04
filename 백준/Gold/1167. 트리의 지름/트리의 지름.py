import sys
input = sys.stdin.readline
from collections import deque

#정점 1 ~ V

# -1 을 만나기 전까지 (정점, 거리) 형태로 주어진다.

N=int(input())
graph=[[] for _ in range(N+1)]

for _ in range(N):
    arr=list(map(int,input().split()))
    start=arr[0]
    i=1
    while arr[i]!=-1:
        node=arr[i]
        dist=arr[i+1]

        graph[start].append((node,dist))
        graph[node].append((start,dist))
        i+=2



def bfs(curr):
    q=deque()
    q.append(curr)
    visited=[-1]*(N+1)
    visited[curr]=0

    while q:
        now=q.popleft()

    
        for nxt,dist in graph[now]:
            if visited[nxt]==-1:
                q.append(nxt)
                visited[nxt]=visited[now]+dist
    far_node=visited.index(max(visited))
    far_dist=max(visited)

    return far_node,far_dist


far,dist=bfs(1)
far,dist=bfs(far)

print(dist)

