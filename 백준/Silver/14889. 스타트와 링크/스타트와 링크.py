import sys
input = sys.stdin.readline
from itertools import combinations,permutations

N=int(input())

power=[]
for _ in range(N):
    power.append(list(map(int,input().split())))

#20개 중에 10개 골라서 거기있는애들끼리 
team=set(range(N))

result=[]

for teamA in combinations(range(N),N//2):
    teamA = set(teamA)
    teamB = team - set(teamA)
    

    scoreA=0
    scoreB=0

    for i,j in combinations(teamA,2):
        scoreA+=power[i][j]+power[j][i]
    
    for i,j in combinations(teamB,2):
        scoreB+=power[i][j]+power[j][i]

    result.append(abs(scoreA-scoreB))
print(min(result))