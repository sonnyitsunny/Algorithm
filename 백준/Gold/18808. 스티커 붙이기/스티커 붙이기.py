import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
notebook = [[0]*M for _ in range(N)]

def rotate(mat):
    # 90도 시계방향 회전
    r, c = len(mat), len(mat[0])
    res = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][r-1-i] = mat[i][j]
    return res

def can_paste(x, y, sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
    return True

def paste(x, y, sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1

def try_place(sticker):
    for _ in range(4):
        r, c = len(sticker), len(sticker[0])
        # 가능한 모든 시작 좌표 시도
        for x in range(N - r + 1):
            for y in range(M - c + 1):
                if can_paste(x, y, sticker):
                    paste(x, y, sticker)
                    return True
        # 회전 후 다시 시도
        sticker = rotate(sticker)
    return False

for _ in range(K):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for __ in range(r)]
    try_place(sticker)

# 붙은 칸 수
print(sum(map(sum, notebook)))
