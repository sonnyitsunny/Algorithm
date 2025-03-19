from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문 여부 및 거리 저장 (초기 위치는 1)
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1  # 시작 위치 방문 처리
    
    # BFS 시작 (x, y)
    queue = deque([(0, 0)])  
    
    while queue:
        x, y = queue.popleft()
        
        # 목표 도착 (맨 끝 위치)
        if x == n-1 and y == m-1:
            return visited[x][y]  # 최단 거리 반환
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1  # 이전 거리 +1
                    queue.append((nx, ny))  # 다음 탐색 위치 추가
    
    return -1  # 도달할 수 없는 경우
