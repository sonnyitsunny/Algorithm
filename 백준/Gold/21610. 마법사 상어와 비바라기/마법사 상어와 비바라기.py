import sys
from collections import deque
input = sys.stdin.readline

#1 이동 시킨다. 여기서 경계 넘어가는 거 잘구현
#2 비를 내린다. +1
#3 비내린 칸의 물복사 시전 
#4 순환하면서 칸이 2 이상인애들을  -2하고 만든다. 단 전에 구름이었던 곳은 제외

#핵심은 구름을 큐로 관리하는 것


#좌 좌상 상 우상 우 우하 하 좌하
dir=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

#대각선 확인
check=[(-1,-1),(-1,1),(1,-1),(1,1)]

N,M=map(int,input().split())
maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))

cloud=deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])


for _ in range(M):
    d,cnt=map(int,input().split())
    d=dir[d-1]

    #이동횟수
    for _ in range(cnt):
        cloud_cnt=len(cloud)
        for _ in range(cloud_cnt):
            x,y=cloud.popleft()
            nx,ny=x+d[0],y+d[1]
            
            # 경계넘어가기
            if nx==N:
                nx=0
            elif nx==-1:
                nx=N-1
            
            if ny==N:
                ny=0
            elif ny==-1:
                ny=N-1   
            cloud.append((nx,ny))

    #비내리자
    for x,y in cloud:
        maps[x][y]+=1

    #물복사
    for x,y in cloud:
        add_rain=0
        for k in range(4):
            nx=x+check[k][0]
            ny=y+check[k][1]

            if 0<=nx<=N-1 and 0<=ny<=N-1:
                if maps[nx][ny]>0:
                    add_rain+=1
        maps[x][y]+=add_rain

    #순환하면서 칸이 2 이상인애들을  -2하고 만든다. 단 전에 구름이었던 곳은 제외
    new_cloud=deque()
    for i in range(N):
        for j in range(N):
            if maps[i][j]>=2 and (i,j) not in cloud:
                maps[i][j]-=2
                new_cloud.append((i,j))
    cloud=new_cloud

answer=0
for row in maps:
    answer+=sum(row)
print(answer)