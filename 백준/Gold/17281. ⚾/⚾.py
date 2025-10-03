import sys
from itertools import permutations
input = sys.stdin.readline

N=int(input())
innings=[]

for _ in range(N):
    innings.append(list(map(int,input().split())))

answer=0

for case in permutations(range(1,9)):
    sequence=list(case[:3])+[0]+list(case[3:])

    score=0
    batter_id=0

    for inning in range(N):
        out=0
        base1,base2,base3=0,0,0
        while out < 3:
            player=sequence[batter_id]
            result=innings[inning][player]

            if result==0:
                out+=1
            elif result==1:
                score+=base3
                base3=base2
                base2=base1
                base1=1
            elif result==2:
                score+=base3
                score+=base2
                base3=base1
                base2=1
                base1=0
            elif result==3:
                score+=base3
                score+=base2
                score+=base1
                base3=1
                base2=0
                base1=0
            elif result==4:
                score+=base3
                score+=base2
                score+=base1
                score+=1
                base3=0
                base2=0
                base1=0

            batter_id=(batter_id+1)%9
    if answer<score:
        answer=score

print(answer)