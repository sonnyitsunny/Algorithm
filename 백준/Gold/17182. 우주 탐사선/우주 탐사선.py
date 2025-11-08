import sys
input = sys.stdin.readline

# 모든 행성을 탐사하는데 걸리는 최소 시간

# 행성수, 발사 위치


# 0시작 해서 dfs해서 
# if i!=j 일 때만 

# dfs(집합,누적시간)



n,k=map(int,input().split())

INF=int(1e8)
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))


for m in range(n):
    for i in range(n):
        for j in range(n):
            space[i][j]=min(space[i][j],space[i][m]+space[m][j])
# for row in space:   
#     print(row)

visited=set()
visited.add(k)

min_time=INF

def dfs(cur,visited,time):
    global min_time
    if time >= min_time:
        return
    if len(visited)==n:
        min_time=min(min_time,time)
        return
    
    for nxt in range(n):
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt,visited,time+space[cur][nxt])
            visited.remove(nxt)



dfs(k,visited,0)
print(min_time)