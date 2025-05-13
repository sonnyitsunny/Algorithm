#하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토
#가장 밑 상자부터 주어짐
# tomato 3차원 배열에 익히기+방문여부 관리, +1해줘서 일수 관리하기, 마지막엔 최대값에서 -1해줘야 함
#근데 토마토에 0이 하나라도 존재한다면 -1출력


from collections import deque


m,n,h=map(int,input().split())
tomato=[]

for _ in range(h):
    f=[]
    for _ in range(n):
        f.append(list(map(int,input().split())))
    tomato.append(f)

#상하좌우, 위,아래
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,1,-1]

q=deque()


# -1아니고 익은 토마토를 대상으로, 일단 큐에 다 집어넣음
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j]!=-1 and tomato[k][i][j]==1:
                q.append((k,i,j))


while q:
    k,i,j=q.popleft()
        
    for z in range(6):
        nk=k+dh[z]
        ni=i+dx[z]
        nj=j+dy[z]

        if 0<=nk<h and 0<=ni<n and 0<=nj<m:
            if tomato[nk][ni][nj]==0:
                tomato[nk][ni][nj]=tomato[k][i][j]+1
                q.append((nk,ni,nj))
                


max_t=0

for w in tomato:
    for row in w:
        max_t=max(max_t,max(row))
        if 0 in row:
            print(-1)
            exit()

print(max_t-1)