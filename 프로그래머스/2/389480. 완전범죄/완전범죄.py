def backtrack(a,b,id,info,dp,n,m):
    
    global answer
    if id==len(info):
        if a<n and b<m:
            answer=min(answer,a)
            return
    
    if (a, b, id) not in dp:
        dp.add((a, b, id))
    else:
        return
    if a>=n or b>=m:
        return
    
    backtrack(a+info[id][0],b,id+1,info,dp,n,m)
    backtrack(a,b+info[id][1],id+1,info,dp,n,m)
    
    
def solution(info, n, m):
    
    global answer
    answer=float('inf')

    
    
    #보유 흔적

    dp=set()
    backtrack(0,0,0,info,dp,n,m)
    
    if answer!=float('inf'):
        return answer
    else:
        return -1
    
    return 