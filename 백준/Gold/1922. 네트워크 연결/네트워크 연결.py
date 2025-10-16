import sys

input = sys.stdin.readline

N=int(input())

M=int(input())

edges=[]
parent=[0]*(N+1)

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    start,end,cost=map(int,input().split())
    edges.append((cost,start,end))

edges.sort()
result=0


def find_p(x):
    if parent[x]!=x:
        parent[x]=find_p(parent[x])
    return parent[x]

def union_p(a,b):
    a=find_p(a)
    b=find_p(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b


for edge in edges:
    cost,a,b=edge

    if find_p(a)!=find_p(b):
        union_p(a,b)
        result+=cost
print(result)