
n=int(input())
#상우하좌
dx=[0,1,0,-1]
dy=[1,0,-1,0]


#오른쪽 위체크
cx=[1,1,0]
cy=[1,0,1]

#오른쪽 아래 체크
kx=[1,1,0]
ky=[-1,0,-1]


for _ in range(n):
    result=[(0,0)]
    x=0
    y=0
    size=0

    
    #인덱스
    mx,my=0,0
    moves=list(input())
    for m in moves:
        if m=='R':
            mx=(mx+1)%4
            my=(my+1)%4
        
        elif m=='L':
            mx=(mx+3)%4
            my=(my+3)%4

        if m=='F':
            x=x+dx[mx]
            y=y+dy[my]
            result.append((x,y))

        elif m=='B':
            x=x-dx[mx]
            y=y-dy[my]
            result.append((x,y))
    max_x=0
    min_x=0
    max_y=0
    min_y=0

    for rx,ry in result:
        max_x=max(max_x,rx)
        min_x=min(min_x,rx)
    
        max_y=max(max_y,ry)
        min_y=min(min_y,ry)
        #print(max_y,min_y)
    print((max_x-min_x)*(max_y-min_y))
    #print((max_x-min_x),(max_y-min_y))