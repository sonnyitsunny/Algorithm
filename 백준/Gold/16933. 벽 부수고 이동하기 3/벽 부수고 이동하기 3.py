import sys
from collections import deque
input=sys.stdin.readline



#False담긴 3차원 배열
#이동 거리는 그냥 큐로 관리
n,m,k=map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
#[][][][0] 낮
#[][][][1] 밤
visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]

q=deque()
visited[0][0][k]=True
q.append((0,0,1,k,True))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#x,y,이동거리,부시기 가능한 수, 낮밤
while q:
    x,y,move,k,day=q.popleft()

    if x==n-1 and y==m-1:
        print(move)
        exit(0)
    
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        nk=k-1
        

        if 0<=nx<n and 0<=ny<m:
            #낮
            if day:
                #부수고 이동
                if graph[nx][ny]==1 and k>0 and not visited[nx][ny][nk]:
                    visited[nx][ny][nk]=True
                    q.append((nx,ny,move+1,nk,False))


                #안 부수고 이동
                elif graph[nx][ny]==0 and not visited[nx][ny][k]:
                    visited[nx][ny][k]=True
                    q.append((nx,ny,move+1,k,False))

            #밤
            else:
                #부수려고 낮까지 기다리는 경우
                if graph[nx][ny]==1 and k>0 and not visited[nx][ny][nk]:
                    q.append((x,y,move+1,k,True))


                #안부수고 그냥 이동
                elif graph[nx][ny]==0 and not visited[nx][ny][k]:
                    visited[nx][ny][k]=True
                    q.append((nx,ny,move+1,k,True))





print(-1)


