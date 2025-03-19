from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
    

    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    else:
        visited=[[False] * w for _ in range(h)]

        maps=[]
        for _ in range(h):
            row=list(map(int,input().split()))
            maps.append(row)

        dx=[-1,1,0,0,-1,-1,1,1]
        dy=[0,0,-1,1,-1,1,-1,1]
        cnt=0
        def dfs(x,y):
            visited[x][y]=True

            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w and not visited[nx][ny]:
                    if maps[nx][ny] == 1:
                        dfs(nx,ny)
            


        for i in range(h):
            for j in range(w):

                if not visited[i][j] and maps[i][j] == 1:
                    dfs(i,j)
                    cnt+=1



        print(cnt)

# print(maps)