import sys
input = sys.stdin.readline
import copy





# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dir=[
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1),
    (1,0),
    (1,1),
    (0,1),
    (-1,1)
]


def find_fish(board,num):
    for i in range(4):
        for j in range(4):
            if board[i][j] and board[i][j][0]==num:
                return (i,j)
    return False

def move_fish(board,shark_x,shark_y):
    for num in range(1,17):
        pos=find_fish(board,num)
        if not pos:
            continue
        x,y=pos
        d=board[x][y][1]
        for _ in range(8):
            nx,ny=x+dir[d][0], y+dir[d][1]
            if 0<=nx<4 and 0<=ny<4 and not (nx==shark_x and ny == shark_y):
                board[x][y][1]=d
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                break
            d=(d+1)%8




def dfs(board,sx,sy,score):
    global answer
    board=copy.deepcopy(board)

    fish_num,shark_dir=board[sx][sy]
    score+=fish_num

    board[sx][sy]=None

    move_fish(board,sx,sy)

    for step in range(1,4):
        nx,ny=sx+dir[shark_dir][0]*step, sy+dir[shark_dir][1]*step
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny]:
            dfs(board,nx,ny,score)
    answer=max(answer,score)


board=[]
for _ in range(4):
    data=list(map(int,input().split()))
    row=[]
    for j in range(4):
        num=data[2*j]
        ds=data[2*j+1]-1
        row.append([num,ds])
    board.append(row)

answer=0
dfs(board,0,0,0)
print(answer)