import sys
input=sys.stdin.readline
from collections import deque
from collections import defaultdict

visited1=[]
def dfs(start_v):
    visited1.append(start_v)
    for v in graph[start_v]:
        if v not in visited1:
            dfs(v)
    return visited1

def bfs(start_v):
    visited=[start_v]
    queue=deque()
    queue.append(start_v)
    while queue:
        cur_v=queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

graph=defaultdict(list)

N,M,start_v=map(int,input().split())

for _ in range(0,M):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for key in graph:
    graph[key].sort()


print(*dfs(start_v))
print(*bfs(start_v))