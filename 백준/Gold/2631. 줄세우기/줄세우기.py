
n=int(input())
arr=[]
dp=[1]*n
for _ in range(n):
    arr.append(int(input()))


for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            dp[j]=max(dp[j],dp[i]+1)

max_v=max(dp)
print(n-max_v)