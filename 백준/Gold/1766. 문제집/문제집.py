import sys
input = sys.stdin.readline
import heapq

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
order=[]

indeg=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indeg[b]+=1

heap=[]
for i in range(1,N+1):
    if indeg[i]==0:
        heapq.heappush(heap,i)

while heap:
    now=heapq.heappop(heap)
    order.append((now))

    for next in graph[now]:
        indeg[next]-=1
        if indeg[next]==0:
            heapq.heappush(heap,next)

print(*order)