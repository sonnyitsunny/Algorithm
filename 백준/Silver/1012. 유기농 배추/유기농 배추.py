import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(i,j):
    dx=[-1,1,0,0]   
    dy=[0,0,-1,1]
    visted[i][j]=True
    for k in range(0,4):
        next_i=i+dx[k]
        next_j=j+dy[k]
        if 0<=next_i<N and 0<=next_j<M:
            if matrix[next_i][next_j]==1 and not visted[next_i][next_j]:
                dfs(next_i,next_j)

#테스트 케이스 받기
T=int(input())

#테스트 케이스 횟수 만큼 수행
for _ in range(0,T):
    #지렁이 수
    cnt=0
    
    # 가로, 세로, 배추 수
    M,N,K=map(int,input().split())
    
    # 크기에 맞게 배추밭 만들어주기
    matrix=[[0 for _ in range(0,M)] for _ in range(0,N)]
    #방문여부 판단
    visted=[[False for _ in range(0,M)] for _ in range(0,N)]
    #배추 수 만큼 반복해서 배추 심기
    for _ in range(0,K):
        X,Y=map(int,input().split())
        matrix[Y][X]=1

    for i in range(0,N):
        for j in range(0,M):
            if matrix[i][j]==1 and not visted[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt)


