import sys
from itertools import permutations, product
from collections import deque
input=sys.stdin.readline


# 상하좌우 위 아래 이동 가능
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

#큐브 만들기
case=[]
for _ in range(5):
    floor=[]
    for _ in range(5):
        floor.append(list(map(int,input().split())))
    case.append(floor)

def rotate90(board):
    n=len(board)
    new_board=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[j][n-i-1]=board[i][j]
    return new_board

rotations = []
for b in case:
    r0 = b
    r1 = rotate90(r0)
    r2 = rotate90(r1)
    r3 = rotate90(r2)
    rotations.append([r0, r1, r2, r3])

def bfs(cube):

    cnt = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    cnt[0][0][0]=0
    q=deque()
    q.append((0,0,0))

    while q:
        z,x,y=q.popleft()
        if z==4 and x==4 and y==4:
            result.append(cnt[4][4][4])
        for k in range(6):
            nz=z+dz[k]
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                #기준은 갈 곳이 cnt로 0, cube로 1이어야함
                if cube[nz][nx][ny]==1 and cnt[nz][nx][ny]==-1:
                    q.append((nz,nx,ny))
                    cnt[nz][nx][ny]=cnt[z][x][y]+1


result=[]
for order in permutations(range(5)):
    for rots in product(range(4),repeat=5):
        cube=[]
        for i in range(5):
            floor = rotations[order[i]][rots[i]]
            cube.append(floor)

        if cube[0][0][0] == 0 or cube[4][4][4] == 0:
            continue

        bfs(cube)

if len(result) > 1:
    print(min(result))
else:
    print(-1)
