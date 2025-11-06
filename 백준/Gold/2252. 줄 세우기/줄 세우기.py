import sys
input = sys.stdin.readline

from collections import deque


N,M=map(int,input().split())
indegree=[0]*(N+1)

graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1

q=deque()
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)

result=[]

while q:
    now=q.popleft()
    result.append(now)

    for nex in graph[now]:
        indegree[nex]-=1
        if indegree[nex]==0:
            q.append(nex)
print(*result)