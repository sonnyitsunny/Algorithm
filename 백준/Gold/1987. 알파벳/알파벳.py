import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26
answer = 0

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - 65
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, cnt + 1)
                visited[idx] = False

visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(answer)
