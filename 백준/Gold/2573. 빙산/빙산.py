from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt(icebergs):
    # 현재 빙산 위치만 녹임
    new_graph = [row[:] for row in graph]
    for x, y in icebergs:
        sea = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    sea += 1
        new_graph[x][y] = max(0, graph[x][y] - sea)
    return new_graph

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

year = 0
while True:
    # 빙산 좌표 수집
    icebergs = [(i, j) for i in range(n) for j in range(m) if graph[i][j] > 0]

    # 빙산이 아예 없으면 종료
    if not icebergs:
        print(0)
        break

    # 덩어리 개수 확인
    visited = [[False] * m for _ in range(n)]
    land = 0
    for x, y in icebergs:
        if not visited[x][y]:
            bfs(x, y, visited)
            land += 1

    if land >= 2:
        print(year)
        break

    # 1년 경과 및 녹이기
    graph = melt(icebergs)
    year += 1
