import sys
sys.setrecursionlimit(10**7)

M,N=map(int,input().split())
board=[]
for _ in range(M):
    board.append(list(map(int,input().split())))

dp=[[-1]*N for _ in range(M)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if x==M-1 and y==N-1:
        return 1
    
    if dp[x][y]!=-1:
        return dp[x][y]

    dp[x][y]=0

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<M and 0<=ny<N:
            if board[nx][ny]<board[x][y]:
                dp[x][y]+=dfs(nx,ny)

    return dp[x][y]

print(dfs(0,0))
