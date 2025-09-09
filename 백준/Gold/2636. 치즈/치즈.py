import sys
input = sys.stdin.readline
from collections import deque

#구멍생성 공기중으로만 이동 0일 때만 이동 ->함수, 리턴값으로 녹여야할 칸좌표 리턴


#치즈조각 칸의 수 세기 -> 함수

#녹이는 거 -> 리턴 받은 값을 꺼내서 -> 0으로 만듬
#시간

#치즈 조각이 없다면 시간 출력 치즈조각 칸의 수 출력


R,C=map(int,input().split())
cheeze=[]
for _ in range(R):
    cheeze.append(list(map(int,input().split())))


def bfs(x,y):
    visited=[[False]*C for _ in range(R)]
    q=deque()
    q.append((x,y))
    visited[x][y]=True

    target=[]
    
    while q:
        x,y=q.popleft()

        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<R and 0<=ny<C:
                #공기중인경우
                if not visited[nx][ny] and cheeze[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append((nx,ny))

                #치즈인경우
                if not visited[nx][ny] and cheeze[nx][ny]==1:
                    visited[nx][ny]=True
                    target.append((nx,ny))

    return target

def cheeze_cnt():
    ans=0
   
    for i in range(R):
        for j in range(C):
            if cheeze[i][j]==1:
                ans+=1
    return ans

cnt=0
time=0
is_cheeze=True

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while is_cheeze:

    #구멍
    targets=bfs(0,0)
    
    #갯수 세기
    cnt=cheeze_cnt()

    #녹이고 시간 추가
    for x,y in targets:
        
        cheeze[x][y]=0
        
    time+=1

    after_cnt=0
    for i in range(R):
        for j in range(C):
            if cheeze[i][j]==1:
                after_cnt+=1
    
    if after_cnt==0:
        is_cheeze=False
        

print(time)
print(cnt)