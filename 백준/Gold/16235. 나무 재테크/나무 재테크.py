import sys
input = sys.stdin.readline


#배열 3개 관리 현재양분, 나무있는 땅, A:양분추가

#나무있는 땅에 groud[r][c]=[나이3 나무, 나이4 나무] 이런식으로
#현재 양분배열을 가져오고 나무땅가져와서 비교하면서나이어린 애부터 양분 먹음 부족->죽음

N,M,K=map(int,input().split())
ground=[[[]for _ in range(N)]for _ in range(N)]

A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

energy=[[5]*N for _ in range(N)]


for _ in range(M):
    r,c,age=map(int,input().split())
    ground[r-1][c-1].append(age)


dirs=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]



def spring_summer():
    for i in range(N):
        for j in range(N):
            trees=ground[i][j]
            ground[i][j]=[]
            
            dead=[]

            if trees:
                trees.sort()

                for t in trees:
                    if energy[i][j]>=t:
                        energy[i][j]-=t
                        ground[i][j].append(t+1)
                    else:
                        dead.append(t//2)
                
                energy[i][j]+=sum(dead)

def fall():
    for i in range(N):
        for j in range(N):
            for tree in ground[i][j]:
                if tree%5==0:
                    for dx,dy in dirs:
                        nx,ny=i+dx,j+dy
                        if 0<=nx<N and 0<=ny<N:
                            ground[nx][ny].append(1)



for _ in range(K):

    #봄,여름 같이함
    spring_summer()


    #가을
    fall()


    #겨울
    for i in range(N):
        for j in range(N):
            energy[i][j]+=A[i][j]



answer=0
for i in range(N):
    for j in range(N):
        answer+=len(ground[i][j])

print(answer)
