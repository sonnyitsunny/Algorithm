import sys
from collections import deque
input=sys.stdin.readline

#동생 이동은 가속 붙음
#위치도 같고 시간도 같아야함

n, k = map(int, input().split())

visited = [[False]*2 for _ in range(500001)]
    
q=deque()
#위치, 시간
q.append((n,0))
visited[n][0]=True
time=0
safe=False
while True:
    
    sister=k+time*(time+1)//2

    if sister>500000:
        print(-1)
        break
    
    if visited[sister][time%2]:
        print(time)
        break

    
    for _ in range(len(q)):
        cur,t=q.popleft()
        for next in (cur*2,cur-1,cur+1):
            if 0<=next<=500000 and not visited[next][(t+1)%2]:
                visited[next][(t+1)%2]=True
                q.append((next,t+1))
    time+=1