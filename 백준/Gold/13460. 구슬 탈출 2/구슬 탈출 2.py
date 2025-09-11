import sys
input = sys.stdin.readline

N,M=map(int,input().split())
maps=[]

for i in range(N):
    row=list(input().strip())
    if "R" in row:
        rx=i
        ry=row.index("R")
    if "B" in row:
        bx=i
        by=row.index("B")

    maps.append(row)

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def move(x,y,dr):
    back=-1
    for cnt in range(1,10):
        nx,ny=x+dx[dr]*cnt,y+dy[dr]*cnt
        if maps[nx][ny]=="#":
            return cnt+back
        if maps[nx][ny]=="O":
            return cnt
        if maps[nx][ny]=="B" or maps[nx][ny]=="R":
            back-=1




def dfs(n,rx,ry,bx,by):
    global ans
    if n>10:
        return 
    
    for dr in range(4):
        #공의 이동거리 계산
        r_cnt = move(rx,ry,dr)
        b_cnt = move(bx,by,dr)
        if r_cnt==0 and b_cnt==0:
            continue
        #이동반영
        nrx,nry=rx+dx[dr]*r_cnt,ry+dy[dr]*r_cnt
        nbx,nby=bx+dx[dr]*b_cnt,by+dy[dr]*b_cnt
        

        if maps[nbx][nby]=="O":
            continue
        else:
            if maps[nrx][nry]=="O":
                ans=min(n,ans)
                return ans
        
        maps[rx][ry],maps[bx][by]='.','.'
        maps[nrx][nry],maps[nbx][nby]='R','B'
        dfs(n+1,nrx,nry,nbx,nby)
        maps[nrx][nry],maps[nbx][nby]='.','.'
        maps[rx][ry],maps[bx][by]='R','B'
        


ans=11
dfs(1,rx,ry,bx,by)
if ans==11:
    ans=-1
print(ans)