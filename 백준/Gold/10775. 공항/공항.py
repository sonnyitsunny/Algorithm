import sys
input = sys.stdin.readline

G=int(input())
P=int(input())
parent=[i for i in range(G+1)]

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
for _ in range(P):
    g=int(input())
    gate=find(g)

    if gate==0:
        break

    ans+=1
    union(gate,gate-1)
print(ans)