import sys
input = sys.stdin.readline


N,M=map(int,input().split())
board=[list(input().strip()) for _ in range(N)]

parent=[i for i in range(N*M)]



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

dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

for i in range(N):
    for j in range(M):
        ni=i+dx[board[i][j]]
        nj=j+dy[board[i][j]]
        a=i*M+j
        b=ni*M+nj
        union(a,b)

roots=set()
for i in range(N*M):
    roots.add(find(i))
print(len(roots))