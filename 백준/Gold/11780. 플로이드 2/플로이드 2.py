import sys
input = sys.stdin.readline

n=int(input())
m=int(input())


INF=int(1e8)
city=[[INF]*(n+1) for _ in range(n+1)]

nxt = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1,n+1):
    city[i][i]=0

for i in range(m):
    a,b,c=map(int,input().split())
    if city[a][b]>c:
        city[a][b]=c
        nxt[a][b]=b
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if city[i][k]+city[k][j]<city[i][j]:
                city[i][j]=city[i][k]+city[k][j]
                nxt[i][j]=nxt[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if city[i][j]==INF:
            print(0,end=' ')
        else:
            print(city[i][j],end=' ')
    
    print()
def get_path(i, j):
    if nxt[i][j] == 0:
        return []
    path = [i]
    while i != j:
        i = nxt[i][j]
        path.append(i)
    return path

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if city[i][j] == INF or i == j:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), *path)