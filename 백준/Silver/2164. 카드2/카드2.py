from collections import deque

import sys
input = sys.stdin.readline


N=int(input())
q=deque()

for i in range(1,N+1):
    q.append(i)

while len(q)>1:
    
    q.popleft()
    if len(q)>=2:
        x=q.popleft()

        q.append(x)

print(q[0])