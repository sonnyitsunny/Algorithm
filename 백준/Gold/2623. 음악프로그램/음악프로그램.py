import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())

graph=[[]for _ in range(N+1)]
indegree=[0]*(N+1)

for _ in range(M):
    arr=list(map(int,input().split()))
    seq=arr[1:]
    for i in range(len(seq)-1):
        graph[seq[i]].append(seq[i+1])
        indegree[seq[i+1]]+=1
order=[]
q=deque()
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    order.append(now)

    for next in graph[now]:
        indegree[next]-=1
        if indegree[next]==0:
            q.append((next))

if len(order)==N:
    for i in order:
        print(i)
else:
    print(0)