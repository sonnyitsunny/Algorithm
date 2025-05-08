#n m r 을 입력받고
#비어있는 2차원 배열을 길이가 n+1개 짜리로 만든다
#False가 담긴 1차원 배열을 길이 n+1 만든다.
#0이 담긴 1차원 배열을 (n+1)개 만든다
#m번 반복한다.
#그래프 만든다.
#bfs
import sys
from collections import deque
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

order=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append(r)
visited[r]=True
cnt=1
order[r]=cnt


for  i in range(1,n+1):
    graph[i].sort()


while q:
    now=q.popleft()

    for next in graph[now]:
        if not visited[next]:
            visited[next]=True
            cnt+=1
            order[next]=cnt
            q.append(next)
for i in range(1,n+1):
    print(order[i])