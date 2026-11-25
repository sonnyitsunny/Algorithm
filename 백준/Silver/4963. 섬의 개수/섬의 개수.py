


from collections import deque

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        x,y=q.popleft()

        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and board[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny))

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    # 1은 땅, 0은 바다
    board=[]
    for _ in range(h):
        row=list(map(int,input().split()))
        board.append(row)
    
    visited=[[False]*(w) for _ in range(h)]
    cnt=0
    
    for i in range(h):
        for j in range(w):
            if board[i][j]==1 and not visited[i][j]:
                cnt+=1
                bfs(i,j)
                
    print(cnt)