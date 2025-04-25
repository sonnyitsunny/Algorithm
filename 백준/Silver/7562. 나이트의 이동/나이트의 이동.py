from collections import deque
#숫자 받는다
#숫자만큼 반복

#체스판 만들기
#처음 위치를 넣는다.

#while문으로 돌린다.
#같다면 그 위치를 출력한다.

n=int(input())
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,-2,-1,1,2]

for _ in range(n):
    l=int(input())
    cur_x,cur_y=map(int,input().split())
    arr_x,arr_y=map(int,input().split())

    maps=[[0]*l for _ in range(l)]
    q=deque()
    q.append((cur_x,cur_y))

    while q:
        cur_x,cur_y=q.popleft()
        if cur_x==arr_x and cur_y==arr_y:
            print(maps[cur_x][cur_y])
            break
        
        for k in range(8):
            n_x,n_y=cur_x+dx[k],cur_y+dy[k]
            if 0<=n_x<l and 0<=n_y<l and not maps[n_x][n_y]:
                maps[n_x][n_y]=maps[cur_x][cur_y]+1
                q.append((n_x,n_y))
