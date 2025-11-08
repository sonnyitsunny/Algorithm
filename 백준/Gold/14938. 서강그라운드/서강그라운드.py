import sys
input = sys.stdin.readline

n,m,r=map(int,input().split())


INF=int(1e8)
city=[[INF]*(n+1) for _ in range(n+1)]
items=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    city[i][i]=0

for i in range(r):
    a,b,c=map(int,input().split())
    if city[a][b]>c:
        city[a][b]=c
        city[b][a]=c
       
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])
                
max_cnt=0

for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        if city[i][j]<=m:
            cnt+=items[j]
    
    max_cnt=max(max_cnt,cnt)

print(max_cnt)