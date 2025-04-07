r,c=map(int,input().split())

maps=[]
for _ in range(r):
    maps.append(list(input()))

visited=[ ['.']*c for _ in range(r)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(r):
    for j in range(c):
        if maps[i][j]=='X':
            cnt=0
            for k in range(4):
                ni,nj=i+dx[k],j+dy[k]
                if ni<0 or ni>=r or nj<0 or nj>=c or maps[ni][nj]=='.':
                    cnt+=1

            if cnt<3:
                visited[i][j]='X'

#print(visited)

min_row=r
max_row=0

min_col=c
max_col=0

for i in range(r):
    for j in range(c):
        if visited[i][j]=='X':
            min_row=min(min_row,i)
            max_row=max(max_row,i)

            min_col=min(min_col,j)
            max_col=max(max_col,j)


for i in range(min_row,max_row+1):
    print(*visited[i][min_col:max_col+1],sep='')
