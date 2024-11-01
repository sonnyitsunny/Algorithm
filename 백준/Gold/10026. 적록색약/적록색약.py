import sys
#input=sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque




N=int(input())

graph=[]

for _ in range(N):
    word=input()
    graph.append(list(word))
#아닌
visited1=[[False for _ in range(N)] for _ in range(N)]
#색약
visited2=[[False for _ in range(N)] for _ in range(N)]

def dfs1(x,y):
    visited1[x][y]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and visited1[nx][ny]!=True and graph[x][y]==graph[nx][ny]:
            dfs1(nx,ny)

def dfs2(x,y):
    visited2[x][y]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and visited2[nx][ny]!=True:
            if graph[x][y]=='B' and graph[x][y]==graph[nx][ny]:
                dfs2(nx,ny)
            if graph[x][y]!='B' and graph[nx][ny]!='B':
                dfs2(nx,ny)


#색약 아닌사람
count1=0
#색약
count2=0
for i in range(N):
    for j in range(N):
        if visited1[i][j]!=True:
            dfs1(i,j)
            count1+=1
        if visited2[i][j]!=True:
            dfs2(i,j)
            count2+=1



print(count1,count2)


#아닌사람 결과 , 색약인사람 결과