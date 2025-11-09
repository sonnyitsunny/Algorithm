import sys
input = sys.stdin.readline

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

result=0
redundant=[[False]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j or j==k or i==k:
                continue
            
            if graph[i][j]>graph[i][k]+graph[k][j]:
                print(-1)
                sys.exit(0)
            elif graph[i][j]==graph[i][k]+graph[k][j]:
                redundant[i][j]=True

for i in range(n):
    for j in range(i+1,n):
        if not redundant[i][j]:
            result+=graph[i][j]

print(result)
