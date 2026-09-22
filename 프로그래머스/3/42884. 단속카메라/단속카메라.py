def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    
    cctv=routes[0][1]
    
    for start,end in routes[1:]:
        if start<=cctv and end>=cctv:
            continue
        
        cctv=end
        answer+=1
            
    
    
    return answer+1