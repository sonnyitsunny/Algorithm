import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
bamboo=[]
for _ in range(n):
    bamboo.append(list(map(int,input().split())))

dr=[(-1,0),(1,0),(0,1),(0,-1)]

dp=[[0]*n for _ in range(n)]

def dfs(x,y):
    if dp[x][y]!=0:
        return dp[x][y]
    
    dp[x][y]=1
    for dx,dy in dr:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n:
            if bamboo[nx][ny]>bamboo[x][y]:
                dp[x][y]=max(dp[x][y],1+dfs(nx,ny))
    return dp[x][y]

ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans,dfs(i,j))
print(ans)