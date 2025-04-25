n=int(input())
maps=[]
for _ in range(n):
    maps.append(list(map(int,input().split())))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if maps[i][k]==1 and maps[k][j]==1:
                maps[i][j]=1
for row in maps:
    print(*row)