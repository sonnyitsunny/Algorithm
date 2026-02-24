import sys
input = sys.stdin.readline

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]

# 0:오, 1:왼, 2:위, 3:아
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
opp = [1, 0, 3, 2]  # 반대 방향

# horses[i] = [r, c, d]
horses = [[0, 0, 0] for _ in range(K + 1)]

# board[r][c] = 말 번호들 (아래 -> 위)
board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(1, K + 1):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    horses[i] = [r, c, d]
    board[r][c].append(i)

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

for turn in range(1, 1001):
    for k in range(1, K + 1):
        r, c, d = horses[k]

        if board[r][c][0] != k:
            continue

        nr, nc = r + dr[d], c + dc[d]

        # 파랑 또는 범위 밖이면 방향 반전 후 재시도
        if (not in_range(nr, nc)) or color[nr][nc] == 2:
            d = opp[d]
            horses[k][2] = d
            nr, nc = r + dr[d], c + dc[d]

            # 또 파랑/범위밖이면 이동 안 함 (방향만 바뀐 채 유지)
            if (not in_range(nr, nc)) or color[nr][nc] == 2:
                continue

        
        moving = board[r][c]
        board[r][c] = []

        # 빨강이면 순서 반전
        if color[nr][nc] == 1:
            moving.reverse()

        # 새 칸에 쌓기
        board[nr][nc].extend(moving)

        # 이동한 말들의 좌표 갱신 
        for h in moving:
            horses[h][0] = nr
            horses[h][1] = nc

        # 종료 조건
        if len(board[nr][nc]) >= 4:
            print(turn)
            sys.exit(0)

print(-1)