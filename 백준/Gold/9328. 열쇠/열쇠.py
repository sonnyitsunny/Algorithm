import sys
from collections import deque
input = sys.stdin.readline

def solve():
    h, w = map(int, input().split())
    
    building = ['.' * (w + 2)]
    for _ in range(h):
        row = input().strip()
        building.append('.' + row + '.')
    building.append('.' * (w + 2))

    # 초기에 가진 열쇠
    key_input = input().strip()
    if key_input == '0':
        keys = set()
    else:
        keys = set(key_input)

    visited = [[False] * (w + 2) for _ in range(h + 2)]
    doors = {chr(c): [] for c in range(ord('A'), ord('Z') + 1)}  # 각 문에 대기 좌표 저장
    q = deque([(0, 0)])
    visited[0][0] = True
    docs = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < h + 2 and 0 <= ny < w + 2):
                continue
            if visited[nx][ny]:
                continue
            cell = building[nx][ny]
            if cell == '*':  # 벽
                continue

            visited[nx][ny] = True

            if cell == '.':  # 빈 공간
                q.append((nx, ny))

            elif cell == '$':  # 문서
                docs += 1
                q.append((nx, ny))

            elif 'a' <= cell <= 'z':  # 열쇠 발견
                if cell not in keys:
                    keys.add(cell)
                    # 대기 중이던 문들 열기
                    for doorx, doory in doors[cell.upper()]:
                        q.append((doorx, doory))
                    doors[cell.upper()].clear()
                q.append((nx, ny))

            elif 'A' <= cell <= 'Z':  # 문 발견
                if cell.lower() in keys:  # 열쇠 있으면 통과
                    q.append((nx, ny))
                else:  # 없으면 대기
                    doors[cell].append((nx, ny))

            else:
                q.append((nx, ny))

    print(docs)


t = int(input())
for _ in range(t):
    solve()
