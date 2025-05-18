from collections import deque
import sys
#input = sys.stdin.readline


n, m = map(int, input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

#broke[][][1] 이 부순거
broke=[[[0]*2 for _ in range(m)] for _ in range(n)]

q=deque()
q.append((0,0,0))
broke[0][0][0]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
safe=False
while q:
    x,y,br=q.popleft()


    if x==n-1 and y==m-1:
        print(broke[x][y][br])
        safe=True
        break



    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        if 0<=nx<n and 0<=ny<m:

            #벽 아니고, 안가본 곳
            if graph[nx][ny]==0 and broke[nx][ny][br]==0:
                broke[nx][ny][br]=broke[x][y][br]+1
                q.append((nx,ny,br))
            # 벽이고 아직 안부쉈으면 
            elif graph[nx][ny] == 1 and br==0 and broke[nx][ny][1]==0:
                broke[nx][ny][1]=broke[x][y][0]+1
                q.append((nx, ny, 1))
if not safe:
    print(-1)