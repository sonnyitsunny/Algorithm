from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(r,c,x,y,maps,visited):
    
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    days=int(maps[x][y])
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            
            if 0<=nx<r and 0<=ny<c:
                if not visited[nx][ny] and maps[nx][ny]!="X":
                    days+=int(maps[nx][ny])
                    visited[nx][ny]=True
                    q.append((nx,ny))
                
    
    return days

def solution(maps):
    answer = []
    r=len(maps)
    c=len(maps[0])
    
    visited = [[False]*c for _ in range(r)]
    
    #bfs 조건은 방문 안한곳 + X가 아닌 곳
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and maps[i][j]!="X":
                cnt=bfs(r,c,i,j,maps,visited)
                answer.append(cnt)
    
    
    if len(answer)==0:
        return [-1]
    answer.sort()
    return answer