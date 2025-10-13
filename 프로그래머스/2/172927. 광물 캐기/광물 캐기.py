def solution(picks, minerals):
    answer = 0
    
    group=[]
    
    #미네랄은 순서 고정인데 지금 최소 피로도 순으로 구하려고 순서바꾸게됨 근데 그러면 원래라면 못캘 뒤에 있는놈이 앞쪽으로
#  올수도 있다.
    cnt=sum(picks)
    if cnt*5<len(minerals):
        minerals=minerals[:cnt*5]
    
    for i in range(0,len(minerals),5):
        group.append(minerals[i:i+5])
        
    score=[]
    
    #어차피 무조건 캐야되는 애들임, 힘든애를 좋은애로 캔다.
    for g in group:
        dia_cnt=g.count("diamond")
        iron_cnt=g.count("iron")
        stone_cnt=g.count("stone")
        score.append((dia_cnt,iron_cnt,stone_cnt))
    score.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    

    
    
    for dia,iron,stone in score:
        
        if picks[0]>0:
            picks[0]-=1
            answer+=dia*1+iron*1+stone*1
        elif picks[1]>0:
            picks[1]-=1
            answer+=dia*5+iron*1+stone*1
        elif picks[2]>0:
            picks[2]-=1
            answer+=dia*25+iron*5+stone*1
    
    
    
    return answer