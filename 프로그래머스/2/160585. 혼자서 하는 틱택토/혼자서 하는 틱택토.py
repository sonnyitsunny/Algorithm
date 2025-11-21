def win(board, t):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == t:
            return True
        if board[0][i] == board[1][i] == board[2][i] == t:
            return True
    if board[0][0] == board[1][1] == board[2][2] == t:
        return True
    if board[0][2] == board[1][1] == board[2][0] == t:
        return True
    return False
    

def solution(board):
    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_cnt += 1
            elif board[i][j] == "X":
                x_cnt += 1

    # 기본 조건: X <= O <= X+1
    if not (x_cnt <= o_cnt <= x_cnt + 1):
        return 0

    o_win = win(board, "O")
    x_win = win(board, "X")

    # 둘 다 승리 → 불가능
    if o_win and x_win:
        return 0

    # O 승리 → O는 X보다 1개 많아야 함
    if o_win and o_cnt != x_cnt + 1:
        return 0

    # X 승리 → O 개수 == X 개수
    if x_win and o_cnt != x_cnt:
        return 0

    # 나머지는 모두 정상
    return 1
