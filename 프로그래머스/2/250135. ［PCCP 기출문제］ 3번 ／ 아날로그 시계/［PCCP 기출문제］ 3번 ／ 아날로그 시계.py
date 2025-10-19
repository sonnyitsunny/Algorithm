def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time=h1*3600+m1*60+s1
    end_time=h2*3600+m2*60+s2
    
    #시작할때
    if start_time==0 or start_time==12*3600:
        answer+=1
        
    while start_time<end_time:
        
        h=start_time/120%360
        m=start_time/10%360
        s=start_time*6%360
        
        if (start_time+1)/120%360==0:
            hn=360
        else:
            hn=(start_time+1)/120%360
        
        if (start_time+1)/10%360==0:
            mn=360
            
        else:
            mn=(start_time+1)/10%360
        
        if (start_time+1)*6%360==0:
            sn=360
        
        else:
            sn=(start_time+1)*6%360
        
        if s<m and mn<=sn:
            answer+=1
        if s<h and hn<=sn:
            answer+=1
        if mn==sn and hn==sn:
            answer-=1
    
        start_time+=1
    
    
    return answer