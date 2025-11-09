import sys
input = sys.stdin.readline


INF=int(1e9)

n,m=map(int,input().split())

dist=[[INF]*(n+1) for _ in range(n+1)]

res=[[0]*(n+1) for _ in range(n+1)]


for i in range(1,n+1):
    dist[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<dist[a][b]:
        dist[a][b]=c
        dist[b][a]=c
        res[a][b]=b
        res[b][a]=a 

for k in range(1, n + 1):          
    for i in range(1, n + 1):     
        for j in range(1, n + 1): 
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                res[i][j]=res[i][k]
                

for i in range(1,n+1):
    for j in range(1,n+1):
        if res[i][j]==0:
            print("-",end=' ')
        else:
            print(res[i][j],end=' ')
    print()