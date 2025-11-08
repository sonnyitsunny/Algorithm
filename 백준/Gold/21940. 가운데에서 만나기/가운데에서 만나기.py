import sys
input = sys.stdin.readline

n,m=map(int,input().split())


INF=int(1e8)
city=[[INF]*(n+1) for _ in range(n+1)]
distance=[0]*(n+1)

for i in range(1,n+1):
    city[i][i]=0

for i in range(m):
    a,b,c=map(int,input().split())
    if city[a][b]>c:
        city[a][b]=c
        
        
       
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])
            
people=int(input())
home=list(map(int,input().split()))


# n번집을 모이는 장소로 할때 거리
for i in range(1,n+1):
    max_round_trip = 0
    #h는 각자 집   
    for h in home:
        if city[h][i] == INF or city[i][h] == INF:
            max_round_trip = INF
            break
        max_round_trip = max(max_round_trip, city[h][i] + city[i][h])
    distance[i] = max_round_trip
target=min(distance[1:])

result=[]
for id,d in enumerate(distance):
    if d==target:
        result.append(id)
result.sort()
#print(distance)
print(*result)