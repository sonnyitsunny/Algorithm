import sys
input = sys.stdin.readline

from collections import deque

N,M=map(int,input().split())
up={}
snake={}

for _ in range(N):
    start,end=map(int,input().split())
    up[start]=end


for _ in range(M):
    start,end=map(int,input().split())
    snake[start]=end


q=deque()
q.append((1,0)) # 현재위치, 주사위 횟수
visited=[False]*101
visited[1]=True

while q:
    position,cnt=q.popleft()
    if position==100:
        print(cnt)
        break
    

    for i in range(1,7):
        next_position=position+i

        if next_position<=100:
            #사다리 타는 경우
            if next_position in up:
                next_position=up[next_position]

            #뱀타는 경우
            elif next_position in snake:
                next_position=snake[next_position]

            #그대로
            if not visited[next_position]:
                visited[next_position]=True
                q.append((next_position,cnt+1))
