import sys
input = sys.stdin.readline
import copy

dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


N,M,K=map(int,input().split())


board=[[[]for _ in range(N)] for _ in range(N)]


for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    board[r-1][c-1].append((m,s,d))



for _ in range(K):
    newboard=[[[]for _ in range(N)] for _ in range(N)]

    #이동
    for i in range(N):
        for j in range(N):
            for m,s,d in board[i][j]:
                nx=(i+s*dir[d][0])%N
                ny=(j+s*dir[d][1])%N
                newboard[nx][ny].append((m,s,d))
    
    #합치기

    for i in range(N):
        for j in range(N):
            if len(newboard[i][j])>=2:
                total_m,total_s,cnt=0,0,len(newboard[i][j])
                even,odd=0,0

                for m, s, d in newboard[i][j]:
                    total_m+=m
                    total_s+=s
                    if d%2==0:
                        even+=1
                    else:
                        odd+=1
                
                newboard[i][j]=[]

                new_m=total_m//5
                

                if new_m==0:
                    continue
                new_s=total_s//cnt

                if even==0 or odd==0:
                    dirs=[0,2,4,6]

                else:
                    dirs=[1,3,5,7]
                
                for nd in dirs:
                    newboard[i][j].append((new_m,new_s,nd))
    board=newboard

answer=0
for r in range(N):
    for c in range(N):
        for m,s,d in board[r][c]:
            answer+=m
print(answer)