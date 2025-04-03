import sys
from collections import deque
N = int(sys.stdin.readline())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(a, b):
    q = deque()
    q.append((a,b))
    distance = [[0]*N for _ in range(N)]
    eat_list = []
    global size
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if pan[nx][ny] <= size and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if pan[nx][ny] < size and pan[nx][ny]!=0:
                    eat_list.append((nx,ny,distance[nx][ny]))
    return eat_list

count = 0
for i, line in enumerate(pan):
    for j, value in enumerate(line):
        if value == 9:
            x=i
            y=j
pan[x][y] = 0
size = 2
eat = 0
while 1:
    visited = [[0]*N for _ in range(N)]
    eat_list = bfs(x,y)
    
    if len(eat_list)<1: # 먹을 수 있는 리스트가 없으면 무한루프 탈출
        break
    eat_list.sort(key=lambda x:(-x[2],-x[0],-x[1])) # 오름차순 정렬 우선순위: 거리, x, y 순
    if len(eat_list)<1: # 먹을 수 있는 리스트가 없으면 무한루프 탈출
        break
    nx,ny,distance = eat_list.pop()
    # 먹은 좌표로 이동시킴
    x = nx
    y = ny
    pan[x][y] = 0
    count += distance # 소요시간 count에 더함
    eat += 1
    if size==eat:
        size += 1
        eat = 0
print(count)