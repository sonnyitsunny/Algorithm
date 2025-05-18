from collections import deque
import sys
#input = sys.stdin.readline
#while문 안에 이중포문
#녹이기 실행 그 녹인 거는 다른 맵에 반영
#녹이기 1년 했으면 year+1하고 bfs로 덩어리 갯수 파악 그게 2이상 이면 year 출력
import copy
n, m = map(int, input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
ice=[[0]*m for _ in range(n)]
year=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def melt(x,y):
    zero_cnt=0
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0:
                zero_cnt+=1
    
    height=graph[x][y]-zero_cnt
    if height<=0:
        ice[x][y]=0
    else:
        ice[x][y]=height

def bfs(x,y):
    visited[x][y]=True
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny]!=0:
                    visited[nx][ny]=True
                    q.append((nx,ny))


safe=False
while True:
    land=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]!=0:
                melt(i,j)
    year+=1
    graph=[]
    for row in ice:
        graph.append(row)

    ice=[[0]*m for _ in range(n)]

    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]>0:
                bfs(i,j)
                land+=1

    if land>=2:
        #print(land)
        print(year)
        #for row in graph:
            #print(row)
        break

    if land==0:
        print(0)
        break



