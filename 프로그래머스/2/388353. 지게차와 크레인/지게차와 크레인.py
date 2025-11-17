from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(container,x,y,n,m):
    
    visited=[[False]*m for _ in range(n)]
    q=deque()
    visited[x][y]=True
    q.append((x,y))
    
    
    
    while q:
        x,y=q.popleft()
        
        #바깥까지 연결
        if x==0 or x==n-1 or y==0 or y==m-1:
            return True
        
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and container[nx][ny]==0:
                visited[nx][ny]=True
                q.append((nx,ny))

    return False


def solution(storage, requests):
    answer = 0
    n=len(storage)
    m=len(storage[0])
    
    #1은 컨테이너 있음, 0은 컨테이너 없음
    container=[[1]*m for _ in range(n)]
    
    for r in requests:
        
        
        #2개면 크레인으로 그냥 다 없앰
        if len(r)==2:
            t=r[0]
            for i in range(n):
                for j in range(m):
                    if storage[i][j]==t:
                        container[i][j]=0  
        #1개인 경우 bfs돌려서 창고외부와 연결된 경우 target에 넣고 나중에 한번에 없앤다.    
        else:
            target=[]
            for i in range(n):
                for j in range(m):
                    if storage[i][j]==r:
                        check=bfs(container,i,j,n,m)
                        if check:
                            target.append((i,j))
            for x,y in target:
                container[x][y]=0
                        
    for row in container:
        answer+=sum(row)
    
    
    return answer