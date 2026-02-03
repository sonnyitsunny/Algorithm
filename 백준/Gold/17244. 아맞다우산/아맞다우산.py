from collections import deque

N,M=map(int,input().split())

board=[]
for _ in range(M):
    board.append(input())

x_index = {}
x_cnt=0

for i in range(M):
    for j in range(N):
        if board[i][j]=='S':
            sr,sc=i,j
        elif board[i][j]=='E':
            er,ec=i,j
        elif board[i][j]=='X':
            x_index[(i,j)] = x_cnt
            x_cnt+=1

ALL=(1<<x_cnt) - 1

visited=[[[False] * (1<<x_cnt) for _ in range(N)] for _ in range(M)]

q=deque()
q.append((sr,sc,0,0))
visited[sr][sc][0]=True

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while q:
    r,c,state,dist = q.popleft()
    if (r,c) == (er,ec) and state ==ALL:
        print(dist)
        break
    for d in range(4):
        nr=r+dr[d]
        nc=c+dc[d]

        if 0<=nr<M and 0<=nc<N and board[nr][nc]!='#':
            new_state=state

            if board[nr][nc]=='X':
                idx=x_index[(nr,nc)]
                new_state |= (1<<idx)
            if not visited[nr][nc][new_state]:
                visited[nr][nc][new_state] = True
                q.append((nr, nc, new_state, dist + 1))