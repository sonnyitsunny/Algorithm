import sys
input=sys.stdin.readline



# 7일에 딱 끝나거나 그전에 끝나는 경우

# 5일 4일 3일 

# 4일 3일 

# 2일 

# 조건은 무조건 t+일소요시간 <=N
# dp[0]=0 1 base id


#dp= 10 20 10 20 15 40 200
#tt= 3 5 1 1 2 4 2
#pp= 10 20 10 20 15 40 200
#0인덱스는 0이라고 치고


#핵심은 dp[i]가 i일 시작 하기 전까지의 최대 이익
N=int(input())

dp=[0]*(N+2) # dp[n+1]일에 n일차에 한 게 반영되어있다.
tt=[0]*(N+1)
pp=[0]*(N+1)

for i in range(1,N+1):
    T,P=map(int,input().split())
    
    tt[i]=T
    pp[i]=P

for i in range(1,N+1):
    dp[i]=max(dp[i],dp[i-1])

    end=i+tt[i]
    if end<=N+1:
        dp[end]=max(dp[end],dp[i]+pp[i])

print(max(dp))