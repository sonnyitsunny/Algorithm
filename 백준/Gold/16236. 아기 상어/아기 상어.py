
from collections import deque
n=int(input())
nofish=0
maps=[] 
#상어위치
shark_x=0
shark_y=0
#상어크기
shark=2

for i in range(n):
    row=list(map(int,input().split()))
    #상어 처음위치
    if 9 in row:
       shark_x=i
       shark_y=row.index(9)
       row[shark_y]=0
    maps.append(row)
    

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(si,sj):
    q=deque()
    v=[[0]*n for _ in range(n)]
    tlst=[]

    q.append((si,sj))
    v[si][sj]=1
    eat=0
    while q:
        ci,cj = q.popleft()
        if eat==v[ci][cj]:
            return tlst,eat-1
        


        for i in range(4):
            ni,nj=ci+dx[i],cj+dy[i]
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and  shark>=maps[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                #나보다 작은 물고기인 경우 tls 추가
                if shark>maps[ni][nj]>0:
                    tlst.append((ni,nj))
                    eat=v[ni][nj]
    #먹을 물고기 못찾음
    return tlst,eat-1


#먹은 수, 거리
cnt=ans=0
while True:
    tlst,dist=bfs(shark_x,shark_y)
    #더 먹을 물고기가 없는 경우
    if len(tlst)==0:
        break
    tlst.sort(key=lambda x:(x[0],x[1]))
    shark_x,shark_y=tlst[0]
    maps[shark_x][shark_y]=0 # 물고기 먹기
    cnt+=1
    ans+=dist
    # 크기만큼 물고기 먹으면 +1
    if shark==cnt:
        shark+=1
        cnt=0

print(ans)