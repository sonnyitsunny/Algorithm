import sys
input = sys.stdin.readline
import heapq


n=int(input())
m=int(input())

INF=int(1e8)

graph=[[] for _ in range(n+1)]

prev=[-1]*(n+1)
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
                prev[neighbor]=now
                heapq.heappush(q,(new_cost,neighbor))




start,end=map(int,input().split())


dijkstra(start)

print(distance[end])
path=[]
cur=end
while cur!=-1:
    path.append(cur)
    cur=prev[cur]
path.reverse()
print(len(path))
print(*path)