import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


board=[]
for _ in range(9):
    board.append(list(map(int,input().strip())))

empty=[]


row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            empty.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            box[(i//3)*3 + (j//3)][num] = True  # 3×3 박스 인덱스


def dfs(idx):
    if idx==len(empty):
        for r in board:
            print(''.join(map(str,r)))
        sys.exit(0)
        



    x,y=empty[idx]
    b = (x//3)*3 + (y//3)
    for num in range(1,10):
        if not row[x][num] and not col[y][num] and not box[b][num]:
            board[x][y] = num
            row[x][num] = col[y][num] = box[b][num] = True

            dfs(idx+1)

            # 백트래킹 되돌리기
            board[x][y] = 0
            row[x][num] = col[y][num] = box[b][num] = False



dfs(0)