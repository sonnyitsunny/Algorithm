import sys
input = sys.stdin.readline


R,C=map(int,input().split())
board=[]
for _ in range(R):
    board.append(list(input().strip()))



dx=[-1,1,0,0]
dy=[0,0,-1,1]
max_cnt=0
arr={board[0][0]}
def dfs(x,y,cnt):
    global max_cnt
    max_cnt=max(max_cnt,cnt)
       



    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] not in arr:
                arr.add(board[nx][ny])
                dfs(nx,ny,cnt+1)
                arr.remove(board[nx][ny])

dfs(0,0,1)  #(지금까지 방문했던 곳들, 지날 수 있는 칸)
print(max_cnt)