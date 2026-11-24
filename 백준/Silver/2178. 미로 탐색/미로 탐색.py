from collections import deque


N,M=map(int,input().split())
board=[]
for _ in range(N):
    row=list(input())
    
    tmp=[]
    for r in row:
        tmp.append(int(r))
    board.append(tmp)

#visited=[[False]*M for _ in range(M)]
#print(board)

q=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q.append((0,0))
board[0][0]=0
while q:
    x,y=q.popleft()
    if x==N-1 and y==M-1:
        print(board[N-1][M-1]+1)
        break

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==1:
                board[nx][ny]=board[x][y]+1
                q.append((nx,ny))