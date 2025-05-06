import sys
from collections import deque
input = sys.stdin.readline  # 빠른 입력 처리
n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    i,j=map(int,input().split())
    graph[i].append(j)

visited=[-1]*(n+1)


result=[]
#x가 시작 하는 곳이니까 처음에 얘를 넣고 시작함
#bfs돌리고 visited[] 기준으로 k랑 같을 때 result에 넣음,

q=deque()
q.append(x)
visited[x]=0
while q:
    now=q.popleft()

    if visited[now]==k:
        result.append(now)
    
    for next in graph[now]:
        if visited[next]==-1:
            visited[next]=visited[now]+1
            #print(next)
            q.append(next)

#print(result)

if len(result)==0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)