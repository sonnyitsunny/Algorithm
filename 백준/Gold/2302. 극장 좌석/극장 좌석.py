import sys
input = sys.stdin.readline


n=int(input())

dp=[0]*(n+1)
dp[0]=1
dp[1]=1



for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
   


m=int(input())

res=1
arr=[]
for _ in range(m):
    arr.append(int(input()))

b=0 #이전 vip
for a in arr:
    #맨앞이 vip
    if a==1:
        b=a
        continue
    if a==n:
        seq=a-b-1
        res*=dp[seq]
        b=a
    if a!=1 and a!=n:
        seq=a-b-1
        res*=dp[seq]
        b=a


#끝이 vip가 아닌 경우

seq=n-b
res*=dp[seq]

print(res)