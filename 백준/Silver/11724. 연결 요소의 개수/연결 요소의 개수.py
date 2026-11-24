import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
for _ in range(M):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

cnt=0

def dfs(now):
    visited[now]=True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)