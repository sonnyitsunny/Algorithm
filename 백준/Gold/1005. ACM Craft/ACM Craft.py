import sys
from collections import deque
input = sys.stdin.readline




T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    cost=[0]+list(map(int,input().split()))
    indegree=[0]*(N+1)
    graph=[[] for _ in range(N+1)]

    dp=[0]*(N+1)

    for _ in range(K):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    W=int(input())
    q=deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            dp[i]=cost[i]
            q.append(i)

    
    while q:
        x=q.popleft()

        for nx in graph[x]:

            dp[nx]=max(dp[nx],dp[x]+cost[nx])
            indegree[nx]-=1
            if indegree[nx]==0:
                q.append(nx)
    print(dp[W])