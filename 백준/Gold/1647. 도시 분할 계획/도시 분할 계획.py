import sys
input = sys.stdin.readline


N,M=map(int,input().split())

edges=[]
parent=[0]*(N+1)

for i in range(1,N+1):
    parent[i]=i
max_cost=0

for _ in range(M):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
    




def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

edges.sort()
total_cost=0
for cost,a,b in edges:
    if find(a)!=find(b):
        union(a,b)
        max_cost=max(max_cost,cost)
        total_cost+=cost
print(total_cost-max_cost)