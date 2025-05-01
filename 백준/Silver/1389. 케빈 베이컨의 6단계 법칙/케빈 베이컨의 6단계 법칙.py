#bfs
#n+1배열만들기, 1부터 n이 될때까지 
#튜플 형태로 저장, 그리고 정렬하며됨

from collections import deque

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

min=999999999

def bfs(start):
    visited=[-1]*(n+1)
    q=deque()
    q.append(start)
    cnt=0
    visited[start]=0

    while q:
        now=q.popleft()

        for next in graph[now]:
            if visited[next]==-1:
                visited[next]=visited[now]+1
                cnt+=visited[next]
                q.append(next)
    return cnt


for i in range(1,n+1):
    cnt=bfs(i)
    if cnt < min:
        min=cnt
        answer = i
print(answer)