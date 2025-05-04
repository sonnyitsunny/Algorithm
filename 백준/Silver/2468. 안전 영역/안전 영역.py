from collections import deque

#맵을 받을 때 반복문 돌면서 max층을 구한다.

#비가 1~ max-1 만큼을 반복문돌린다.

#함수로 구현, 맵을 넘겨주고 내부에서 전용맵을 따로 새로 만든다.
    #맵에 값을 비와 비교해서 잠기면 0 안잠기면 1로 전용맵에 표시한다.
    #방문여부 리스트 만든다.
    #반복문으로 맵 돌면서 안잠긴 부분인 경우+방문 안한 곳
    #bfs호출, 
    #호출 돌 때마다 +1 해서 result리스트에 담음

#result 최대값 출력


N=int(input())
max_height=1
result=[]
maps=[]
for _ in range(N):
    row=list(map(int,input().split()))
    max_height=max(max_height,max(row))
    maps.append(row)

#비내리기
def make_rain(maps,rain):
    tmp=[[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if maps[i][j]>rain:
                tmp[i][j]=1

    return tmp

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(tmp,x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        for k in range(4):
            n_x,n_y=x+dx[k],y+dy[k]
            if 0<=n_x<N and 0<=n_y<N and not visited[n_x][n_y] and tmp[n_x][n_y]==1:
                visited[n_x][n_y]=True
                q.append((n_x,n_y))
                

#강수량 별로 다 구하기
for rain in range(max_height):
    tmp=make_rain(maps,rain)
    visited=[[False]*N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and tmp[i][j]==1:
                bfs(tmp,i,j)
                cnt+=1
    result.append(cnt)
#print(result)
print(max(result))