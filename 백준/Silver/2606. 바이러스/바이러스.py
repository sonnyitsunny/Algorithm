from collections import deque


N=int(input())
M=int(input())

com=[0]*(N+1)

graph=[[]for _ in range(N+1)]

for _ in range(M):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(now):
    com[now]=1
    for nxt in graph[now]:
        if com[nxt]==0:
            com[nxt]=1
            dfs(nxt)


dfs(1)
print(sum(com)-1)