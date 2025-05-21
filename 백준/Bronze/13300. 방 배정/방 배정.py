import sys
input=sys.stdin.readline

n,k=map(int,input().split())

#행 0은 여자, 행1은 남자
rooms=[[0]*7 for _ in range(2)]
#print(rooms)


for _ in range(n):
    s,y=map(int,input().split())
    rooms[s][y]+=1
cnt=0 

for i in range(2):
    for j in range(1,7):
        enough=rooms[i][j]//k
        more=rooms[i][j]%k
        if more==0:
            cnt+=enough
        else:
            cnt=cnt+enough+1
print(cnt)