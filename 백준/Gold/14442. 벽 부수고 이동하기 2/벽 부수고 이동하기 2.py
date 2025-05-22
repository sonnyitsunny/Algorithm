import sys
from collections import deque
input=sys.stdin.readline



#False담긴 3차원 배열
#이동 거리는 그냥 큐로 관리
n,m,k=map(int,input().split())
graph=[]
for _ in range(n):
    row=input().strip()
    graph.append(list(map(int,row)))
visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]

q=deque()
visited[0][0][k]=True
q.append((0,0,1,k))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y,move,k=q.popleft()

    if x==n-1 and y==m-1:
        print(move)
        exit(0)
    
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        nk=k-1

        #벽을 부수고 가는 경우
        if k>0:
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny][nk] and graph[nx][ny]==1:
                visited[nx][ny][nk]=True
                q.append((nx,ny,move+1,nk))

        #그냥 가는 경우
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny][k] and graph[nx][ny]!=1:
            visited[nx][ny][k]=True
            q.append((nx,ny,move+1,k))

print(-1)


