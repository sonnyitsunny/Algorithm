import sys
input = sys.stdin.readline

N,g=input().split()
N=int(N)

cnt=0
limit=0

games={"Y":1,
       "F":2,
       "O":3}

names={}

for _ in range(N):
    player=input().strip()  
    if player not in names:
        names[player]=1
        limit+=1
        if limit==games[g]:
            limit=0
            cnt+=1

print(cnt)