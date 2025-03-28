from collections import deque
from copy import deepcopy
R,C,T=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

pos=[]
for i in range(R):
    if arr[i][0]==-1:
        pos.append((i,0))
        


for _ in range(T):
    arr_t=deepcopy(arr)
    #확산
    for i in range(R):
        for j in range(C):
            if arr[i][j]>4:
                t=arr[i][j]//5

                for k in range(4):
                    ni,nj=i+dx[k],j+dy[k]
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj]!=-1:
                        arr_t[i][j]-=t
                        arr_t[ni][nj]+=t

    arr=arr_t
    #순환
    i1,i2=pos[0][0],pos[1][0]
    for i in range(i1-1,0,-1):
        arr[i][0]=arr[i-1][0]
    for j in range(0,C-1,1):
        arr[0][j]=arr[0][j+1]
    for i in range(0,i1,1):
        arr[i][C-1]=arr[i+1][C-1]
    for j in range(C-1,0,-1):
        arr[i1][j]=arr[i1][j-1]



    for i in range(i2+1,R-1,1):
        arr[i][0]=arr[i+1][0]
    for j in range(0,C-1,1):
        arr[R-1][j]=arr[R-1][j+1]
    for i in range(R-1,i2,-1):
        arr[i][C-1]=arr[i-1][C-1]
    for j in range(C-1,0,-1):
        arr[i2][j]=arr[i2][j-1]
    arr[i1][1]=0
    arr[i2][1]=0
ans=sum(map(sum,arr))+2

print(ans)