def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        tmp=0
        while True:
            if tmp==n:
                answer+=1
                break
            elif tmp>n:
                break
            tmp+=i
            i+=1
    
    
    
    
    return answer