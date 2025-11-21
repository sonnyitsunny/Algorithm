from collections import deque
def solution(board):
    
    r=len(board)
    c=len(board[0])
    
    for i in range(r):
        for j in range(c):
            if board[i][j]=="R":
                start=(i,j)
            elif board[i][j]=="G":
                end=(i,j)
    
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q=deque()
    q.append((start[0],start[1],0)) #위치와 장애물에 튕한 횟수(미끄러짐 무빙)
    min_cnt=1e9
    visited=[[False]*c for _ in range(r)]
    visited[start[0]][start[1]]=True
    while q:
        #튕겨져 나온 위치와 지금까지 튕겨진 횟수
        x,y,cnt=q.popleft()
        
        if x==end[0] and y==end[1]:
            return cnt
        
        
        for k in range(4):
            move_x=dx[k] #x이동량
            move_y=dy[k] #y이동량
            start_x=x
            start_y=y
            
            while True:
                if start_x+move_x>=r or start_x+move_x<0 or 0>start_y+move_y or start_y+move_y>=c:
            
                    break
                elif board[start_x+move_x][start_y+move_y]=="D":
                   
                    break
                
                start_x=start_x+move_x
                start_y=start_y+move_y
            if not visited[start_x][start_y]:
                visited[start_x][start_y]=True
            
            
                q.append((start_x,start_y,cnt+1))
    

    return -1
