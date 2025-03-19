from itertools import combinations
from collections import deque
import sys
import copy

input = sys.stdin.readline


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]


empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virus_positions = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]


def bfs(new_lab):
    queue = deque(virus_positions)  
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 4방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2  # 감염 확산
                queue.append((nx, ny))

    
    return sum(row.count(0) for row in new_lab)


max_safe_area = 0
for walls in combinations(empty_spaces, 3):  
    new_lab = copy.deepcopy(lab)  

    
    for x, y in walls:
        new_lab[x][y] = 1
    
    
    safe_area = bfs(new_lab)
    max_safe_area = max(max_safe_area, safe_area)


print(max_safe_area)
