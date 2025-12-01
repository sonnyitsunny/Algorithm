import sys
input = sys.stdin.readline

def blank(x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            board[i][j]=" "



def divide(x,y,size):
    if size==1:
        return
    
    new=size//3

    for i in range(3):
        for j in range(3):
            nx=x+i*new
            ny=y+j*new

            if i==1 and j==1:
                blank(nx,ny,new)
            else:
                divide(nx,ny,new)



n=int(input())
board=[['*']*n for _ in range(n)]

divide(0,0,n)


for row in board:
    print("".join(row))