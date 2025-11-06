import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())
board=[list(input().strip()) for _ in range(N)]
dirs=[(-1,0),(1,0),(0,-1),(0,1)]

group=[[-1]*M for _ in range(N)]
group_size=[]
group_id=0

def bfs(x,y,gid):
    q=deque([(x,y)])
    group[x][y]=gid
    size=1
    while q:
        cx,cy=q.popleft()
        for dx,dy in dirs:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<N and 0<=ny<M and board[nx][ny]=="0" and group[nx][ny]==-1:
                group[nx][ny]=gid
                size+=1
                q.append((nx,ny))
    return size

for i in range(N):
    for j in range(M):
        if board[i][j]=='0' and group[i][j]==-1:
            size=bfs(i,j,group_id)
            group_size.append(size)
            group_id+=1

res=[['0']*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]=="1":
            near=set()
            for dx,dy in dirs:
                nx,ny = i+dx,j+dy
                if 0<=nx<N and 0<=ny<M and group[nx][ny]!=-1:
                    near.add(group[nx][ny])
            val=1+sum(group_size[g] for g in near)
            res[i][j]=str(val%10)

for row in res:
    print(''.join(row))