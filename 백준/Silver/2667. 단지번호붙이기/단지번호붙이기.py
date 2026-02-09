from collections import deque

n=int(input())
city=[]
for _ in range(n):
    city.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False]*n for _ in range(n)]
#print(visited)

result=[]
#1이 이미 있으니까 2부터 단지를 준다.
start=2

def bfs(x,y,start):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    city[x][y]=start
    while q:
        x,y=q.popleft()

        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if city[nx][ny]==1:
                    city[nx][ny]=start
                    visited[nx][ny]=True
                    q.append((nx,ny))            

for i in range(n):
    for j in range(n):
        if not visited[i][j] and city[i][j]==1:
            bfs(i,j,start)
            start+=1
result=[]
for t in range(2,start+1):
    cnt=0
    for i in range(n):
        for j in range(n):
            if city[i][j]==t:
                cnt+=1
    result.append(cnt)
result.sort(key=lambda x:x)
print(len(result)-1)
for r in result[1:]:
    print(r)