def solution(mats, park):
    #안되면 -1이니까 기본으로
    answer = -1
    #가장 큰 돗자리니까,mats를 내림차순 정렬
    mats.sort(reverse=True)
    park_x=len(park)
    park_y=len(park[0])
    
    
    #mats마다 반복문을 수행
    for m in mats:
        for start_x in range(park_x):
            for start_y in range(park_y):
                if park[start_x][start_y]!="-1":
                    continue
                safe = True
                for cur_x in range(m):
                    for cur_y in range(m):
                        if start_x+cur_x>=park_x or start_y+cur_y>=park_y:
                            safe=False
                            break
                            
                        if park[start_x+cur_x][start_y+cur_y]!="-1":
                            safe=False
                            break
                        
                    if not safe:
                        break
                if safe:
                    answer=m
                    return answer
    
    
    return answer