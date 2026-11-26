from collections import deque
N=int(input())
q=deque()
import sys
input = sys.stdin.readline
for _ in range(N):
    com=list(input().split())
    if com[0]=="push":
        q.append(int(com[1]))

    elif com[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif com[0]=="back":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif com[0]=="pop":
        if q:
            x=q.popleft()
            print(x)
        else:
            print(-1)
    elif com[0]=="size":
        print(len(q))
    elif com[0]=="empty":
        if q:
            print(0)
        else:
            print(1)