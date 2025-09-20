import sys
from collections import deque,defaultdict
input = sys.stdin.readline



N,K=map(int,input().split())

board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))

pos=[] #번호 좌표 방향
top=defaultdict(list)

#말을 0번말부터 k-1번말까지
for i in range(1,K+1):
    r,c,d=map(int,input().split())
    pos.append((i-1,r-1,c-1,d-1))
    top[(r-1,c-1)].append(i-1)

# 0 1 2 3 
# 우 좌 상 하
dir=[(0,1),(0,-1),(-1,0),(1,0)] 


#0은 흰색, 1은 빨간색, 2는 파란색
turn=1
limit=False
while turn <=1000:
    for i in range(K):
        num, r, c, d = pos[i]
        nr,nc=r+dir[d][0],c+dir[d][1]
        
        #파랑인경우
        if nr<0 or nr>=N or nc<0 or nc>=N or board[nr][nc]==2:
            
            if pos[num][3]==0 or pos[num][3]==1:
                next_d=(d+1)%2
                pos[num]=(num,r,c,next_d) # 방향 바꾸기
            else:
                if pos[num][3]==2:
                    pos[num]=(num,r,c,3)
                    
                elif pos[num][3]==3:
                    pos[num]=(num,r,c,2)
            
            d=pos[num][3]
            nr,nc=r+dir[d][0],c+dir[d][1]
            # 반대 방향도 파란색이거나 범위 밖이면 그냥 멈춤
            if nr<0 or nr>=N or nc<0 or nc>=N or board[nr][nc]==2:
                continue


        if 0<=nr<N and 0<=nc<N:
            #흰색인경우
            if board[nr][nc]==0:
                #지금 내위치에서 내가 맨 밑인 경우 다 데려감
                if top[(r,c)][0]==num:
                    arr=top[(r,c)]
                    
                    for num in arr:
                        pos[num]=(num,nr,nc,pos[num][3])
                        
                        top[(nr,nc)].append(num)
                    top[(r,c)]=[]
                
                #지금 내 위치에서 내가 맨 밑이 아닌 경우 나 + 내 위에 데려감
                else:
                    id=top[(r,c)].index(num)
                    down=top[(r,c)][:id]
                    up=top[(r,c)][id:]
                    top[(r,c)]=down
                    
                    
                    for num in up:
                        pos[num]=(num,nr,nc,pos[num][3])
                        top[(nr,nc)].append(num)
                    
            #빨강인 경우    
            elif board[nr][nc]==1:
                #지금 내위치에서 내가 맨 밑인 경우 다 데려감
                if top[(r,c)][0]==num:
                    arr=top[(r,c)]
                    arr.reverse()

                    for num in arr:
                        pos[num]=(num,nr,nc,pos[num][3])
                        top[(nr,nc)].append(num)
                    top[(r,c)]=[]
                
                #지금 내 위치에서 내가 맨 밑이 아닌 경우 나 + 내 위에 데려감, 근데 역순으로
                else:
                    id=top[(r,c)].index(num)
                    down=top[(r,c)][:id]
                    up=top[(r,c)][id:]
                    top[(r,c)]=down
                    
                    
                    up.reverse()
                    for num in up:
                        pos[num]=(num,nr,nc,pos[num][3])
                        top[(nr,nc)].append(num)


        #4층탑 여부 확인
        if len(top[(nr,nc)])>=4:
            limit=True
            break

        
    #턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료
    if limit:
        break


    turn+=1

if limit:
    print(turn)
else:
    print(-1)