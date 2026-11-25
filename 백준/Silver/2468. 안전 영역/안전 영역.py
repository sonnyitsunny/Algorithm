


from collections import deque


N=int(input())

board=[]
max_rain=0
for _ in range(N):
    row=list(map(int,input().split()))
    board.append(row)
    max_rain=max(max_rain,max(row))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

res=[]


def bfs(x,y,cnt):
    q=deque()
    visited[x][y]=cnt
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==0 and board[nx][ny]>rain:
                    visited[nx][ny]=cnt
                    q.append((nx,ny))

# 1~ max_rain
for rain in range(max_rain+1):
    #cnt=0 시작
    cnt=0
    visited=[[0]*(N) for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j]>rain:
                cnt+=1
                bfs(i,j,cnt)


    res.append(cnt)

    #bfs + visited

    # cnt출력이 개수  res.append(cnt)

print(max(res))
