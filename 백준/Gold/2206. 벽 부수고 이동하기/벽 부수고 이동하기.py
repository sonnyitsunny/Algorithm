from collections import deque

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input())))


board=[[[0]*2 for _ in range(M)] for _ in range(N)] #[][][1] 이 벽뚫은거임


q=deque()
board[0][0][0]=1
q.append((0,0,0))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

safe=False

while q:
    x,y,br=q.popleft()

    if x==N-1 and y==M-1:
        print(board[N-1][M-1][br])
        exit()
        

    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            #벽없는 경우
            if graph[nx][ny]==0 and board[nx][ny][br]==0:
                board[nx][ny][br]=board[x][y][br]+1
                q.append((nx,ny,br))

            elif graph[nx][ny]==1 and br==0 and board[nx][ny][1]==0:
                board[nx][ny][1]=board[x][y][0]+1
                q.append((nx,ny,1))

print(-1)