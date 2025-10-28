from collections import deque
def solution(maps):
    answer = -1
    
    r=len(maps)#행의 수
    c=len(maps[0])
    visited=[[-1]*c for _ in range(r)]
    
    #시작점은 0초
    start_x,start_y=0,0
    for i in range(r):
        for j in range(c):
            if maps[i][j]=="S":
                start_x,start_y=i,j
    # print(start_x,start_y)
    q=deque()
    q.append((start_x,start_y))
    
    visited[start_x][start_y]=0
    
    
    dr=[(-1,0),(1,0),(0,-1),(0,1)]
    L=False
    
    Lx,Ly=0,0
    
    while q:
        x,y=q.popleft()
        
        if maps[x][y]=="L":
            L=True
            Lx,Ly=x,y
            tmp=visited[x][y]
            visited=[[-1]*c for _ in range(r)]
            visited[Lx][Ly]=tmp
            break
        
        for dx,dy in dr:
            nx,ny=x+dx,y+dy
            
            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny]!="X" and visited[nx][ny]==-1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                    
    if L:
        
        lq=deque()
        lq.append((Lx,Ly))
        while lq:
            x,y=lq.popleft()
            
            if maps[x][y]=="E":
                answer=visited[x][y]
                break

            for dx,dy in dr:
                nx,ny=x+dx,y+dy

                if 0<=nx<r and 0<=ny<c:
                    if maps[nx][ny]!="X" and visited[nx][ny]==-1:
                        visited[nx][ny]=visited[x][y]+1
                        lq.append((nx,ny))

    return answer