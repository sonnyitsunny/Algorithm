N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_cnt = 64  # 최대 8*8칸 전부 다 바꾸는 경우

for i in range(N - 7):        # 8칸씩 자르기
    for j in range(M - 7):
        w_start = 0  # 왼쪽 위가 W로 시작한다고 가정
        b_start = 0  # 왼쪽 위가 B로 시작한다고 가정

        for r in range(8):
            for c in range(8):
                curr = board[i + r][j + c]
                # (r+c)합이 짝수면 왼쪽 위와 같은 색, 홀수면 반대색이 와야 함
                if (r + c) % 2 == 0:
                    if curr != 'W':  # W로 시작했는데 현재 칸이 W가 아님 
                        w_start += 1
                    if curr != 'B':  # B로 시작했는데 현재 칸이 B가 아님 
                        b_start += 1
                else:
                    if curr != 'B':
                        w_start += 1
                    if curr != 'W':
                        b_start += 1

        min_cnt = min(min_cnt, w_start, b_start)

print(min_cnt)
