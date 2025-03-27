from collections import deque


n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#외부공기 여부

def outside_air():
    visited=[[False]*m for _ in range(n)]
    q=deque([(0,0)])
    visited[0][0]=True

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append((nx,ny))

    return visited



def melt(visited):
    to_melt=[]
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                count=0
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if 0<=nx<n and 0<=ny<m:
                        if visited[nx][ny] and graph[nx][ny]==0:
                            count+=1
                if count>=2:
                    to_melt.append((x,y))
    
    for x,y in to_melt:
        graph[x][y]=0
    return len(to_melt)


time=0
while True:
    visited=outside_air()
    melted=melt(visited)
    if melted==0:
        break
    time+=1
print(time)