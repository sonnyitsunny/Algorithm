import sys
from collections import deque
input = sys.stdin.readline


n,m,p=map(int,input().split())
s=[0]+list(map(int,input().split()))
graph=[list(input().strip()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=[deque() for _ in range(p+1)]

for i in range(n):
    for j in range(m):
        if graph[i][j].isdigit():
            target=int(graph[i][j])
            q[target].append((i,j))

while True:
    safe=False

    for target in range(1,p+1):
        move=s[target]
        in_q=deque()

        while q[target] and move:
            for _ in range(len(q[target])):
                x,y=q[target].popleft()

                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if graph[nx][ny]=='.':
                            graph[nx][ny]=str(target)
                            in_q.append((nx,ny))
                            safe=True

            move-=1
            q[target]=in_q
    if not safe:
        break
 
result=[0]*(p+1)

for i in range(n):
    for j in range(m):
        if graph[i][j]!='#' and graph[i][j]!='.':
            cattle=int(graph[i][j])
            result[cattle]+=1
result.pop(0)
print(*result)
# for row in graph:
#     print(row)