import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue=deque([start])
    color[start]=1

    while queue:
        x=queue.popleft()
        for nx in graph[x]:
            if color[nx]==0:
                color[nx]=-color[x]
                queue.append((nx))
            elif color[nx]==color[x]:
                return False
    return True



K=int(input())
for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    color=[0]*(V+1)

    for _ in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    ok=True
    for i in range(1,V+1):
        if color[i]==0:
            if not bfs(i):
                ok=False
                break
    
    print("YES" if ok else "NO")