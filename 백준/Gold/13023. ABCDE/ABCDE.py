import sys
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*N
safe=False

def dfs(cur,depth):
    #print(*result)
    global safe
    visited[cur]=True
    
    if depth==5:
        safe=True
        return 

    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt,depth+1)
    visited[cur]=False

for i in range(N):
    result=[i]
    dfs(i,1)
    if safe:
        break
        
if safe:
    print(1)
else:
    print(0)