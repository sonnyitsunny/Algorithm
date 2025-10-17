import sys
import heapq

input = sys.stdin.readline

V,E=map(int,input().split())

graph=[[] for _ in range(V+1)]
visited=[False]*(V+1)


for _ in range(E):
    start,end,cost=map(int,input().split())
    graph[start].append((cost,end))
    graph[end].append((cost,start))

def prim(x):
    res=0
    visited[x]=True
    heap=graph[x]
    heapq.heapify(heap)
    while heap:
        cost,node=heapq.heappop(heap)

        if not visited[node]:
            res+=cost
            visited[node]=True

            for next_cost,next_node in graph[node]:
                if not visited[next_node]:
                    heapq.heappush(heap,(next_cost,next_node))
    return res


print(prim(1))