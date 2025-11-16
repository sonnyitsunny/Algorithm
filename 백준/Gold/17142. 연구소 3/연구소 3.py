import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

# 2위치를 받아서 
cand=[]

N,M=map(int,input().split())
board=[]
zero_cnt=0

for i in range(N):
    row=list(map(int,input().split()))
    for j in range(N):
        if row[j]==2:
            cand.append((i,j))
            row[j]=0
    

    board.append(row)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

min_time=1e8




for com in combinations(cand,M):
    
    real_virus=set()
    
    
    possible=True
    visited=[[-1]*N for _ in range(N)]
    q=deque()
    for c in com:
        q.append((c[0],c[1]))
        visited[c[0]][c[1]]=0
        real_virus.add((c[0],c[1]))
    
    off_virus=set(cand)-real_virus
    
    while q:
        x,y=q.popleft()
        
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]

            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 and visited[nx][ny]==-1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
    

    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1 and board[i][j]==0 and (i,j) not in cand:
                possible=False
    
    
    if possible:
        max_time=0
        for i in range(N):
            for j in range(N):
                if board[i][j]==0 and (i,j) not in off_virus:
                    max_time=max(max_time,visited[i][j])
        min_time=min(max_time,min_time)

if min_time==1e8:
    print(-1)
else:
    print(min_time)