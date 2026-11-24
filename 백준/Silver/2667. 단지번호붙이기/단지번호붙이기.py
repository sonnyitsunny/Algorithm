N=int(input())

board=[]
for _ in range(N):
    board.append(list(map(int,input())))



number=2

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def dfs(x,y):
   
    board[x][y]=number

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny]==1:
                dfs(nx,ny)



for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            dfs(i,j)
            number+=1

# for r in board:
#     print(r)
print(number-2)
res=[0]*(number)

for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            res[board[i][j]]+=1

res.sort()
for i in range(2,number):
    print(res[i])

