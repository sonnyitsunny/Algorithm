import sys
input = sys.stdin.readline

INF=int(1e9)

edges=[]

N,M=map(int,input().split())

for _ in range(M):
    a,b,c=map(int,input().split())

    edges.append((a,b,c))

start=1

distance=[INF]*(N+1)
distance[start]=0

cycle=False

for i in range(N-1):
    for a,b,cost in edges:
        if distance[a]!=INF and distance[a]+cost<distance[b]:
            distance[b]=distance[a]+cost
    
for a,b,cost in edges:
    if distance[a]!=INF and distance[a]+cost<distance[b]:
        cycle=True
    
if cycle:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])