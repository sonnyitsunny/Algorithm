import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())

graph=[[[] for _ in range(N)] for _ in range(N)]


for _ in range(M):
    x,y,a,b=map(int,input().split())
    graph[x-1][y-1].append((a-1,b-1))

light=[[False]*N for _ in range(N)]
light[0][0]=True

visited=[[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
            return True
    return False

def bfs():
    
    q=deque()
    q.append((0,0))
    visited[0][0]=True

    while True:
        changed=False

        while q:
            x,y=q.popleft()

            for a,b in graph[x][y]:
                if not light[a][b]:
                    light[a][b]=True
                    if check(a,b):
                        visited[a][b] = True
                        q.append((a,b))
                        changed=True

            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if light[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny]=True
                        q.append((nx,ny))
                        changed=True
        if not changed:
            break
bfs()
cnt=0
for row in light:
    cnt+=row.count(True)
print(cnt)