import sys
input = sys.stdin.readline
import heapq



n,k=map(int,input().split())

jewels=[]  #(무게, 가치)
bags=[]

for _ in range(n):
    m,v=map(int,input().split())
    jewels.append((m,v))

for _ in range(k):
    bags.append(int(input()))



jewels.sort()  
bags.sort()

pq=[]
id=0
total=0

for bag in bags:
    while id<n and jewels[id][0]<=bag:
        heapq.heappush(pq,-jewels[id][1])
        id+=1

    if pq:
        total+=-heapq.heappop(pq)
print(total)
