import sys
import heapq
input = sys.stdin.readline

INF=int(1e9)



V,E=map(int,input().split())

start=int(input())

graph=[[] for _ in range(V+1)]


dist=[INF]*(V+1)

for _ in range(E):
    u,v,w=map(int,input().split())

    graph[u].append((v,w))


def dijkstra(start):
    q=[]
    dist[start]=0

    heapq.heappush(q,(0,start))

    while q:
        d,now=heapq.heappop(q)

        if dist[now]<d:
            continue

        for near,cost in graph[now]:
            new_cost=d+cost
            if new_cost<dist[near]:
                dist[near]=new_cost
                heapq.heappush(q,(new_cost,near))

dijkstra(start)


for i in range(1,V+1):
    if start==i:
        print(0)
    elif dist[i]!=INF:
        print(dist[i])
    else:
        print("INF")