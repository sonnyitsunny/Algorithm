N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c][dir]: r행 c열에 방향 dir으로 올 수 있는 경우의 수
# dir: 0 = 가로, 1 = 세로, 2 = 대각선
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 시작 위치: (0, 1) 가로 방향
dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):  # (0,0)-(0,1)은 이미 시작 위치니까 c는 2부터
        if board[r][c] == 1:  # 벽이면 무시
            continue

        # 가로 방향으로 올 수 있는 경우
        dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]

        # 세로 방향은 r이 1 이상일 때만 가능
        if r >= 1:
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]

        # 대각선 방향으로 오려면 왼쪽, 위쪽, 현재 셀이 다 0이어야 함
        if r >= 1 and board[r-1][c] == 0 and board[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

# 마지막 위치에 도달하는 모든 방향의 수를 합쳐서 출력
print(sum(dp[N-1][N-1]))
