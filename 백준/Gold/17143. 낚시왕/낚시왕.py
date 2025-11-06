import sys
input = sys.stdin.readline

R,C,M=map(int,input().split())

ocean=[ [[] for _ in range(C)] for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]
total_size=0
for _ in range(M):
    r,c,s,d,z=map(int,input().split())
    ocean[r-1][c-1].append([s,d-1,z])


def move():
    new_ocean=[ [[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if ocean[i][j]:
                s,d,z=ocean[i][j][0]
                x=i
                y=j
                if s>0:
                    if d in (0,1):
                        s=s%(2*(R-1))

                    else:
                        s=s%(2*(C-1))

                    for _ in range(s):
                        nx,ny=x+1*dx[d],y+1*dy[d]
                        if 0<=nx<R and 0<=ny<C:
                            x,y=nx,ny
                        else:
                            if d==0:
                               d=1
                            elif d==1:
                                d=0
                            elif d==2:
                                d=3
                            else:
                                d=2
                            nx,ny=x+1*dx[d],y+1*dy[d]
                            x,y=nx,ny
                            
                    new_ocean[x][y].append([s,d,z])
                else:
                    new_ocean[x][y].append(ocean[i][j][0])
    return new_ocean

def eat():
    for i in range(R):
        for j in range(C):
            if len(ocean[i][j])>=2:
                sharks=ocean[i][j]
                sharks.sort(key=lambda x:(-x[2]))
                ocean[i][j]=[sharks[0]]


for i in range(C):
    for j in range(R):
        if ocean[j][i]:
            total_size+=ocean[j][i][0][2]
            ocean[j][i]=[]
            break

    
    ocean=move()
    
    eat()



print(total_size)