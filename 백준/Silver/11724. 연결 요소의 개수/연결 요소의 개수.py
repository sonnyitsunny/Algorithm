from collections import deque
import sys

input = sys.stdin.readline
n,m=map(int,(input().split()))
graph=[[] for _ in range(n+1)]
cnt=0
visited=[False] * (n+1)


def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


for _ in range(m):
    x,y=map(int,(input().split()))
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    if not visited[i]:
        bfs(graph,i,visited)
        cnt+=1

print(cnt)



