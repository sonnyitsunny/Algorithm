from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 섬마다 번호 붙이기
def label_island(x, y, idx):
    q = deque()
    q.append((x, y))
    graph[x][y] = idx
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = idx
                q.append((nx, ny))

idx = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            label_island(i, j, idx)
            idx += 1

# 2. 모든 섬 가장자리에서 BFS
def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = 0
                q.append((i, j))

    ans = float('inf')
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 바다일 경우 계속 전진
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y]  # 퍼져나감
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 다른 섬을 만났을 때
                elif graph[nx][ny] != 0 and graph[nx][ny] != graph[x][y]:
                    ans = min(ans, dist[x][y] + dist[nx][ny])

    return ans

print(bfs())
