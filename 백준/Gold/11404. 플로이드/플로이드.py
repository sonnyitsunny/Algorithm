import sys
import heapq

input = sys.stdin.readline


n=int(input())
m=int(input())

INF=int(1e9)

dist=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dist[i][i]=0


for _ in range(m):
    start,end,cost=map(int,input().split())
    if dist[start][end]>cost:
    
        dist[start][end]=cost

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j]==INF:
            print(0,end=' ')
            continue
        print(dist[i][j],end=' ')

    
    
    print()