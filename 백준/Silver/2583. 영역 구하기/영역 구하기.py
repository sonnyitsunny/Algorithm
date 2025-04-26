from collections import deque

# 입력
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

# 색칠된 직사각형 처리
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

# 이동 방향 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1  # 방문 표시
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

# 메인
areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            areas.append(bfs(i, j))

# 출력
areas.sort()
print(len(areas))
print(*areas)
