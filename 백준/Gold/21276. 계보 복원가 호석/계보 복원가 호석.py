import sys
input = sys.stdin.readline
from collections import deque


n=int(input())

names=list(input().split())
names.sort()

idx={}

for i,name in enumerate(names):
    idx[name]=i

m=int(input())

indeg=[0]*n
graph=[[]for _ in range(n)]


for _ in range(m):
    a,b=input().split()
    graph[idx[b]].append(idx[a])
    indeg[idx[a]]+=1

children=[[]for _ in range(n)]
q=deque()
root=[]

for i in range(n):
    if indeg[i]==0:
        root.append(names[i])
        q.append(i)

while q:
    now=q.popleft()

    for nxt in graph[now]:
        indeg[nxt]-=1
        if indeg[nxt]==0:
            q.append((nxt))
            children[now].append(names[nxt])

print(len(root))
print(*root)
for i in range(n):
    children[i].sort()
    print(names[i],len(children[i]),*children[i])