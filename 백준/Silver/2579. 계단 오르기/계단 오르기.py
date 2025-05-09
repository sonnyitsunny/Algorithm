import sys
input=sys.stdin.readline


score={}
sum_score={}


N = int(input())

for i in range(0,N):
    score[i+1]=int(input())

if N==1 :
    sum_score={1:score[1]}
    print(sum_score[N])
elif  N==2:
    sum_score={1:score[1], 2: score[1]+score[2]}
    print(sum_score[N])

elif  N==3:
    sum_score={1:score[1], 2: score[1]+score[2],3:max(score[3]+score[2],score[3]+score[1])}
    print(sum_score[N])

else:

    sum_score={1:score[1], 2: score[1]+score[2],3:max(score[3]+score[2],score[3]+score[1])}
    
    for i in range(4,N+1):
        sum_score[i]=max(score[i]+sum_score[i-2],score[i]+sum_score[i-3]+score[i-1])




    print(sum_score[N])