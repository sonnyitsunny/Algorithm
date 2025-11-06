import sys
input = sys.stdin.readline


N=int(input())

edges=[]
parent=[0]*(N)

for i in range(0,N):
    parent[i]=i

arr=[]
for i in range(N):
   x,y,z=(map(int,input().split()))
   arr.append((x,y,z,i))
edges=[]

for d in range(3):
    arr.sort(key=lambda v:v[d])
    for i in range(N-1):
        cost=abs(arr[i][d]-arr[i+1][d])
        a=arr[i][3]
        b=arr[i+1][3]
        edges.append((cost,a,b))

edges.sort()

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

total_cost=0
for cost,a,b in edges:
    if find(a)!=find(b):
        union(a,b)
        
        total_cost+=cost
print(total_cost)