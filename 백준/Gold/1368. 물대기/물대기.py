import sys
input = sys.stdin.readline


N=int(input())

edges=[]
parent=[0]*(N+1)

for i in range(N+1):
    parent[i]=i

for i in range(N):
    cost=int(input())
    edges.append((cost,0,i+1))
P=[]
for _ in range(N):
    P.append(list(map(int,input().split())))

for i in range(N):
    for j in range(i + 1, N):  
        cost = P[i][j]
        edges.append((cost, i + 1, j + 1))

edges.sort()

total_cost=0

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


for cost,a,b in edges:
    if find(a)!=find(b):
        union(a,b)
        total_cost+=cost
print(total_cost)