import sys
input=sys.stdin.readline

T,W=map(int,input().split())

drop=[]
for _ in range(T):
    d=int(input())
    drop.append(d)
drop=[0]+drop

dp=[[0]*(W+1) for _ in range(T+1)]

#w가 짝수면 1번, 홀수면 2번 나무에.
for t in range(1,T+1):
    for w in range(W+1):
        if w%2==0:
            pos=1
        else:
            pos=2
        
        if pos==drop[t]:
            plus=1
        else:
            plus=0
        if w==0:
            dp[t][w]=dp[t-1][w]+plus
        else:   
            dp[t][w]=max(dp[t-1][w],dp[t-1][w-1])+plus

print(max(dp[t]))