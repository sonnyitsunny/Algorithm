

import sys
input = sys.stdin.readline

from collections import deque
N=int(input())

dq=deque()

for _ in range(N):
    com=list(map(int,input().split()))
    
    
    if com[0]==1:
        dq.appendleft(com[1])

    elif com[0]==2:
        dq.append(com[1])

    elif com[0]==3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif com[0]==4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif com[0]==5:
        print(len(dq))
    
    
    elif com[0]==6:
        if dq:
            print(0)
        else:
            print(1)

    elif com[0]==7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif com[0]==8:
        if dq:
            print(dq[-1])
        else:
            print(-1)