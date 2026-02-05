
# 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸
#(1,1) -> (N,M) - 1 based index

from collections import deque

N,M=map(int,input().split()) 
board=[]
for _ in range(N):
    board.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[-1]*M for _ in range(N)]

q=deque()
visited[0][0]=1
q.append((0,0))

while q:
    x,y = q.popleft()

    if x==N-1 and y==M-1:
        print(visited[N-1][M-1])
        break
    
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==-1 and board[nx][ny]==1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))