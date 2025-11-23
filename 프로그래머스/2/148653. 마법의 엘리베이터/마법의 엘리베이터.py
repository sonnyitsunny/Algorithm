def solution(storey):
    answer=0
    
    while storey:
        
        digit=storey%10
        next_digit=(storey//10)%10
        
        if digit>5:
            answer+=(10-digit)
            storey+=10-digit
            
        
        elif digit<5:
            answer+=(digit)
            storey-=digit
            
        else:
            if next_digit>=5:
                answer+=digit
                storey+=digit
            else:
                answer+=digit
                storey-=digit
        
        storey=storey//10
    
    
    return answer