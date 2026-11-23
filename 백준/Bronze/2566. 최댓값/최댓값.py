board=[]
for _ in range(9):
    board.append(list(map(int,input().split())))

max_v=-1

x=0
y=0
for i in range(9):
    for j in range(9):
        if board[i][j]>max_v:
            max_v=max(board[i][j],max_v)
            x=i+1
            y=j+1
print(max_v)
print(x,y)