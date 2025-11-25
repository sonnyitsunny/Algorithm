import sys
from collections import deque
input = sys.stdin.readline


def check(x,y,nx,ny):
    return abs(x-nx)+abs(y-ny)<=1000




T=int(input())
for _ in range(T):
    n=int(input())
    
    home=tuple(map(int,input().split()))
    points=[]
    for _ in range(n):
        sx,sy=map(int,input().split())
        points.append((sx,sy))
    gx,gy=map(int,input().split())
    points.append((gx,gy))
   
    possible=False
    visited=[False]*(n+1)
    q=deque()
    q.append(home)


    while q:
        x,y=q.popleft()

        if (x,y)==(gx,gy):
            possible=True
            break

        for i in range(n+1):
            if not visited[i] and check(x,y,points[i][0],points[i][1]):
                visited[i]=True
                q.append(points[i])





    if possible:
        print("happy")
    else:
        print("sad")