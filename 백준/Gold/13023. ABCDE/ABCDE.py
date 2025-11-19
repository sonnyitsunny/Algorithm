import sys
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N)]


for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result=[]
visited=[False]*N

safe=False

def dfs(cur):
    #print(*result)
    global safe
    if len(result)==5:
        safe=True
        return 

    for nxt in graph[cur]:
        if not visited[nxt]:
            result.append(nxt)
            visited[nxt]=True
            dfs(nxt)
            result.pop()
            visited[nxt]=False


for i in range(N):
    result=[i]
    visited[i]=True
    dfs(i)
    visited[i]=False

    if safe:
        break
        
if safe:
    print(1)
else:
    print(0)