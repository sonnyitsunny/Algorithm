import sys
input=sys.stdin.readline

#d가 0 북  dx -1, dy 0
# 1 동        0    1   
# 2 남        1      0
# 3 서        0     -1

cnt=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def clean(i,j,d):
    global cnt
    
    if home[i][j]==0:
        home[i][j]=2
        cnt+=1

    for k in range(4):
        next_d=(d+3)%4
        next_i = i+dx[next_d]
        next_j = j+dy[next_d]

        if home[next_i][next_j]==0:
            clean(next_i,next_j,next_d)
            return
        d=next_d
    
    next_d=(d+2)%4
    next_i=i+dx[next_d]
    next_j=j+dy[next_d]

    if home[next_i][next_j]==1:
        return
    clean(next_i,next_j,d)
    
home=[]
N,M=map(int,input().split())
i,j,d=map(int,input().split())

for _ in range(0,N):
    home.append(list(map(int,input().split())))

clean(i,j,d)
print(cnt)