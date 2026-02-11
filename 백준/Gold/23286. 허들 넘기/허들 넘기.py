
INF = int(1e15)
N,M,T=map(int,input().split())
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N+1):
    dist[i][i]=0

for _ in range(M):
    u,v,w=map(int,input().split())
    dist[u][v]=w

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j]=min(dist[i][j],max(dist[i][k],dist[k][j]))

for _ in range(T):
    s,e=map(int,input().split())
    if dist[s][e]==INF:
        print(-1)
    else:
        print(dist[s][e])