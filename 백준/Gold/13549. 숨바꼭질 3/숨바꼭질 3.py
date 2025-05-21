import sys
from collections import deque
input=sys.stdin.readline

# 위치 확인 


n,k=map(int,input().split())
visited=[False]*(100001)

q=deque()
q.append((n,0)) # 수빈이 위치랑 시간 넣기
visited[n]=True

while q:
    subin,time=q.popleft()
    if subin==k:
        print(time)
        break

    for move in (subin*2,subin-1,subin+1):
        if 0<=move<=100000 and not visited[move]:
            if move==subin*2:
                
                
                visited[move]=True
                q.append((move,time))
                
                #print(1)
            elif move==subin+1:
                
             
                visited[move]=True
                q.append((move,time+1))
                #print(2)
            elif move==subin-1:
                
                visited[move]=True
                q.append((move,time+1))
                #print(3)


