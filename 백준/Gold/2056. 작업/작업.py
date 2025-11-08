import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
graph=[[] for _ in range(n+1)]
indeg=[0]*(n+1)
time=[0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    cnt=data[1]

    for pre in data[2:]:
        graph[pre].append(i)
        indeg[i]+=1

q=deque()
dp=[0]*(n+1)

for i in range(1,n+1):
    if indeg[i]==0:
        q.append(i)
        dp[i]=time[i]
while q:
    cur=q.popleft()
    for nxt in graph[cur]:
        indeg[nxt]-=1
        dp[nxt]=max(dp[nxt],dp[cur]+time[nxt])
        if indeg[nxt]==0:
            q.append((nxt))
print(max(dp))