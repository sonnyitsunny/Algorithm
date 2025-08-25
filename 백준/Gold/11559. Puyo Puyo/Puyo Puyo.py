import sys
input=sys.stdin.readline
from collections import deque


maps=[]

for _ in range(12):
    maps.append(list(input().strip()))



#연쇄 횟수
chain=0

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,color,visited):
    q=deque()
    visited[x][y]=True
    q.append((x,y))
    group=[(x,y)]
    
    while q:
        x,y=q.popleft()

        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<12 and 0<=ny<6:
                if not visited[nx][ny] and maps[nx][ny]==color:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    group.append((nx,ny))
    return group

def falling():
    
    for col in range(6):
        stack=[]
        for row in range(11,-1,-1):
            if maps[row][col]!=".":
                stack.append(maps[row][col])
        id=11
        for elem in stack:
            maps[id][col]=elem
            id-=1
        for i in range(id,-1,-1):
            maps[i][col]="."
        




#방문 여부를 한턴돌때마다 초기화 해줘야함
while True:
    visited = [[False]*6 for _ in range(12)]
    target=[]

    for i in range(12):
        for j in range(6):
            if maps[i][j]!="." and not visited[i][j]:
                group=bfs(i,j,maps[i][j],visited)
                if len(group)>=4:
                    target.extend(group)
    if not target:
        break

#폭발
    for x,y in target:
        maps[x][y]="."

    
#떨어지기
    falling()
    chain+=1
print(chain)