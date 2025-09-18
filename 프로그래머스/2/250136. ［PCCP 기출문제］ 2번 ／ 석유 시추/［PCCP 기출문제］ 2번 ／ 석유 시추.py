from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(land):

    def bfs(x,y,num):
        
        visited[x][y]=True
        cnt=1
        q=deque()
        q.append((x,y))
        land[x][y]=num
        
        while q:
            x,y=q.popleft()
            
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if not visited[nx][ny] and land[nx][ny]==1:
                        cnt+=1
                        visited[nx][ny]=True
                        land[nx][ny]=num
                        q.append((nx,ny))
                        
        return cnt
        
    
    answer = 0
    n=len(land) #세로길이
    m=len(land[0]) #가로길이
    
    #효율성 위해서 0이 아닐때 bfs시작하고 land[i][j]을 키값으로 사전에서 그 석유 덩어리 양 구하기
    oil_dict={}
    num=2
    visited=[[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]==1:
                oil_dict[land[i][j]]=bfs(i,j,num)
                num+=1
                
    for j in range(m):
        seen=set()
        oil=0
        for i in range(n):
            if land[i][j]>1 and land[i][j] not in seen:
                seen.add(land[i][j])
                oil += oil_dict[land[i][j]]
        answer=max(oil,answer)
    return answer