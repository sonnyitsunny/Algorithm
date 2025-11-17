import sys
input = sys.stdin.readline
from collections import deque

def bfs(sx, sy, board, h, w):
    dist = [[-1] * w for _ in range(h)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0


    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != 'x' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist
    

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    board=[]
    points=[]

    for i in range(h):
        row=list(input().strip())
        for j in range(w):
            if row[j]=='o':
                points.insert(0,(i,j))
            elif row[j]=='*':
                points.append((i,j))
        board.append(row)

    n=len(points) #로봇 + 먼지
    d=n-1 # 먼지

    if d==0:
        print(0)
        continue

    dist=[[0]*n for _ in range(n)]
    unreachable=False


    for i in range(n):
        sx,sy=points[i]
        dmap = bfs(sx, sy, board, h, w)
        for j in range(n):
            tx,ty=points[j]
            dist[i][j]=dmap[tx][ty]
    
    for j in range(1,n):
        if dist[0][j]==-1:
            unreachable=True
            break
    if unreachable:
        print(-1)
        continue

    INF = 10**9
    dp = [[INF] * (1 << d) for _ in range(n)]
    dp[0][0] = 0

    for mask in range(1 << d): 
        for pos in range(n):
            if dp[pos][mask] == INF:
                continue
            
            for nxt in range(1, n):
                bit = nxt - 1

                if mask & (1 << bit):
                    continue
                if dist[pos][nxt] == -1:
                    continue
                new_mask = mask | (1 << bit)
                new_cost = dp[pos][mask] + dist[pos][nxt]
                if new_cost < dp[nxt][new_mask]:
                    dp[nxt][new_mask] = new_cost
    FULL = (1 << d) - 1
    ans = min(dp[pos][FULL] for pos in range(n))
    print(ans if ans != INF else -1)