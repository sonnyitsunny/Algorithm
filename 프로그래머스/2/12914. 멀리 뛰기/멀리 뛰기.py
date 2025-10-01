
def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[1]=1
    
    
    if n>=2:
        dp[2]=2
        for i in range(2,n):
            dp[i+1]=dp[i]+dp[i-1]
        
    
    answer=dp[n]%1234567
    return answer