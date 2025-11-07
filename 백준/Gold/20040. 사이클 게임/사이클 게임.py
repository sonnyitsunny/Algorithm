import sys
input = sys.stdin.readline

N,M=map(int,input().split())
parent=[i for i in range(N)]

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

ans=0
for i in range(M):
    a,b=map(int,input().split())
    if find(a)==find(b):
        ans=i+1
        break
    union(a,b)
print(ans)