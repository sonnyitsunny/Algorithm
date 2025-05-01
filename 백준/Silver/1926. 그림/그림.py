
from collections import deque

n,m=map(int,input().split())
visited=[[False]*m for _ in range(n)]
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#그림수
cnt=0
#그림 넓이 담을 리스트
result=[0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y] = True
    total=1
    while q:
        x,y=q.popleft()
        for k in range(4):
            n_x,n_y=x+dx[k],y+dy[k]
            if 0<=n_x<n and 0<=n_y<m:
                if graph[n_x][n_y]==1 and not visited[n_x][n_y]:
                    total+=1
                    visited[n_x][n_y]=True
                    q.append((n_x,n_y))

    return total

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1 :
            result.append(bfs(i,j))
            cnt+=1
            
result.sort(reverse=True)
print(cnt)
print(result[0])