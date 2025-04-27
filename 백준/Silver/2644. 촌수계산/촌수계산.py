from collections import deque

n=int(input())

a,b=map(int,input().split())
graph=[[] for _ in range(n+1)]

m=int(input())

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[-1]*(n+1)

q=deque()
q.append(a)
visited[a]=0
while q:
    now=q.popleft()

    for next in graph[now]:
        if visited[next]==-1:
            visited[next]=visited[now]+1
            q.append(next)

print(visited[b])