

import sys
input = sys.stdin.readline
from collections import deque


N=int(input())
res=[]
q=deque()

ds=list(map(int,input().split()))
e=list(map(int,input().split()))

for i in range(N):
    if ds[i]==0:
        q.appendleft(e[i])


M=int(input())
C=list(map(int,input().split()))

for c in C:
    q.append(c)
for _ in range(M):
    res.append(q.popleft())
print(*res)
