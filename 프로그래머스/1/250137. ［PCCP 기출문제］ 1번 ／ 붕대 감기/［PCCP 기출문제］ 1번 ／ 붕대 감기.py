def solution(bandage, health, attacks):

    health_limit=health
    
    time=0
    seq=0
    
    #어택에서 하나씩 가져옴
    for attack in attacks:
        
        #어택[0]이 되기 직전까지 힐 과정 수행,
        while attack[0]!=time:
            #1초당 회복
            health+=bandage[1]
            seq+=1
            #연속하면 추가 회복
            if seq==bandage[0]:
                health+=bandage[2]
                seq=0
            #초과 불가능
            if health>health_limit:
                health=health_limit
            
            
            time+=1
    
        #어택[0]=time 되면 공격함,이때 체력 확인 dead여부 (0이하되면)
        health-=attack[1]
        
        if health <= 0:
            health=-1
            break
        
        seq=0
        time+=1
            
            
    
    
    
    
    
    return health