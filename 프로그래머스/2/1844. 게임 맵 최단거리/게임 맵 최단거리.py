#bfs로 풀고 리스트에 얼마나걸렸는지 넣어서 관리하고 최소 뽑음 근데 최소가 0이면 그냥 -1반환하도록

from collections import deque

def solution(maps):
    answer = -1
    
    n=len(maps)
    m=len(maps[0])
    #방문한곳은 1 방문하지 않은 곳은 0으로 visited 여부확인
    visited=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(0)
        visited.append(row)    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue=deque([(0,0,1)])
    
    while queue:
        x,y,cnt=queue.popleft()
        if x==n-1 and y==m-1:
            return cnt
            
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<=n-1 and 0<=ny and ny<=m-1:
                if maps[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1     
                    queue.append((nx,ny,cnt+1))
    
    
    return answer