import sys
input = sys.stdin.readline


R,C=map(int,input().split())
gas=[]
for _ in range(R):
    gas.append(list(input().strip()))

dr=[(-1,1),(0,1),(1,1)]
res=0
visited=[[False]*C for _ in range(R)]


def dfs(r,c):
    if c==C-1:
        return True
    
    for dx,dy in dr:
        nx,ny=r+dx,c+dy
        if 0<=nx<R and 0<=ny<C:
            if gas[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=True
                if dfs(nx,ny):
                    return True
    return False



for i in range(R):
    if dfs(i,0):
        res+=1
print(res)