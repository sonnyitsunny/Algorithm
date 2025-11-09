import sys
input = sys.stdin.readline
import heapq


n,m,x=map(int,input().split())

times=[0]*(n+1)
INF=int(1e8)






graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)



for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for neighbor,cost in graph[now]:
            new_cost = cost+dist
            if new_cost<distance[neighbor]:
                distance[neighbor]=new_cost
                
                heapq.heappush(q,(new_cost,neighbor))
dijkstra(x)
for i in range(1,n+1):
    times[i]=distance[i]

for i in range(1,n+1):
    distance=[INF]*(n+1)
    dijkstra(i)
    times[i]+=distance[x]


print(max(times))