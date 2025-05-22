import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
visited=[-1]*(100001)
path=[-1]*(100001)
q=deque()
q.append(n)
visited[n]=0

while q:
    subin=q.popleft()
    if subin==k:
        print(visited[subin])
        
        break
    for move in (subin-1,subin+1,subin*2):
        if 0<=move<=100000:
            if visited[move]==-1:
                visited[move]=visited[subin]+1
                path[move]=subin
                q.append(move)
        
        
result=[]
now=k
while now!=-1:
    result.append(now)
    now=path[now]
result.reverse()
print(*result)