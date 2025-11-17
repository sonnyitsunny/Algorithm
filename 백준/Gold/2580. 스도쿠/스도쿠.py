import sys
input = sys.stdin.readline

board=[]
for _ in range(9):
    board.append(list(map(int,input().split())))

empty=[]



for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            empty.append((i, j))


def possible(x, y, n):
    # 행 체크
    for i in range(9):
        if board[x][i] == n:
            return False

    # 열 체크
    for i in range(9):
        if board[i][y] == n:
            return False

    # 3x3 박스 체크
    bx = (x // 3) * 3
    by = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[bx + i][by + j] == n:
                return False

    return True

def dfs(idx):
    if idx==len(empty):
        for r in board:
            print(*r)
        sys.exit(0)
        

    x,y=empty[idx]
   
    for num in range(1, 10):
            if possible(x, y, num):
                board[x][y] = num
                dfs(idx + 1)
                board[x][y] = 0  



dfs(0)