from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
parent=[0]*(n+1)
visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)



def dfs(node):
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            parent[next_node]=node
            dfs(next_node)

dfs(1)

for i in range(2,n+1):
    print(parent[i])