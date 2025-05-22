import sys
input=sys.stdin.readline
from collections import deque

k=int(input())

w,h=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(h)]
visited=[[[False]*(k+1) for _ in range(w)]for _ in range(h)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

hx=[-2,-1, 2,1,-1,-2,1,2]
hy=[-1,-2,-1,-2,2,1,2,1]

q=deque()
q.append((0,0,0,k))
visited[0][0][k]=True

#이동은 0만 가능
while q:
    x,y,move,k=q.popleft()
    
    if x==h-1 and y==w-1:
        print(move)
        exit(0)
    if k>0:
        for i in range(8):
            nx,ny=x+hx[i],y+hy[i]
            nk=k-1
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny][nk] and graph[nx][ny]!=1:
                visited[nx][ny][nk]=True
                q.append((nx,ny,move+1,nk))
    
    for j in range(4):
        nx,ny=x+dx[j],y+dy[j]
        if 0<=nx<h and 0<=ny<w and not visited[nx][ny][k] and graph[nx][ny]!=1:
            visited[nx][ny][k]=True
            q.append((nx,ny,move+1,k))

print(-1)

#말처럼 이동

#상하좌우 이동