V=int(input())
E=int(input())

graph=[[]for _ in range(V+1)]
visited=[False]*(V+1)

for _ in range(E):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(com):
    visited[com]=True

    for nxt_com in graph[com]:
        if not visited[nxt_com]:
            dfs(nxt_com)
    
    
    return sum(visited)


print(dfs(1)-1)