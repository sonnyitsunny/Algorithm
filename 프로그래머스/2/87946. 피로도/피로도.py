from itertools import permutations
def solution(k, dungeons):
    answer = -1
    n=len(dungeons)
    arr=list(permutations(dungeons,n))
    
    for dungeon in arr:
        #print(dungeon)
        tmp=0
        body=k
        for dun in dungeon:
            #print(dun)
            
            if body>=dun[0]:
                body-=dun[1]
                tmp+=1
            
            
            
        answer=max(tmp,answer)
    
    
    
    return answer