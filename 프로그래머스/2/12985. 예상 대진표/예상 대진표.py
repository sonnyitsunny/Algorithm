def solution(n,a,b):
    answer = 1
    
    
    while True:
        if a%2==0:
            a=a//2
        else:
            a=a//2+1
            
        if b%2==0:
            b=b//2
        else:
            b=b//2+1
            
        if a==b:
            break
        else:
            answer+=1

    
    return answer