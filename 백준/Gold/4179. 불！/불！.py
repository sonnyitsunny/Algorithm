

import sys
input=sys.stdin.readline
from collections import deque

r,c=map(int,input().split())
#불
fire=[[-1]*c for _ in range(r)]
#지훈
jihun=[[-1]*c for _ in range(r)]

fq=deque()
jq=deque()

graph = [list(input().strip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fq.append((i, j))
            fire[i][j] = 0
        elif graph[i][j] == 'J':
            jq.append((i, j))
            jihun[i][j] = 0

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#불번지기
while fq:
    x,y=fq.popleft()
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny]!='#' and fire[nx][ny]==-1:
                fire[nx][ny]=fire[x][y]+1
                fq.append((nx,ny))


#지훈도망
while jq:
    x,y=jq.popleft()

    if x==0 or x==r-1 or y==0 or y==c-1:
        print(jihun[x][y]+1)
        exit()
    
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny]!='#' and jihun[nx][ny]==-1:
                if fire[nx][ny] ==-1 or jihun[x][y]+1 < fire[nx][ny]:
                    jihun[nx][ny]=jihun[x][y]+1
                    jq.append((nx,ny))
print("IMPOSSIBLE")