import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(0,4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if matrix[nx][ny]!=0 and matrix[nx][ny]==1:
                    matrix[nx][ny]=matrix[x][y]+1
                    queue.append((nx,ny))
                else:
                    continue
            else:
                continue
    return matrix[N-1][M-1]

N,M=map(int,input().split())

matrix=[]
for _ in range(0,N):
    matrix.append(list(map(int,input().strip())))

print(bfs(0,0))