#2의 위치 (x,y) 구함
#2의 위치를 시작으로 bfs
#maps 만들고
#visited=[[0]*m for _ in range(n)]
#로해서 visited[x][y]=0으로 놓고 시작


from collections import deque

n,m=map(int,input().split())
maps=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    row=list(map(int,input().split()))
    maps.append(row)
    if 2 in row:
        x=i
        y=row.index(2)

visited=[[-1]*m for _ in range(n)]
q=deque()
q.append((x,y))
visited[x][y]=0

while q:
    x,y=q.popleft()
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and visited[nx][ny]==-1:
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            print(0,end=' ')
        else:
            print(visited[i][j],end=' ')

    print()