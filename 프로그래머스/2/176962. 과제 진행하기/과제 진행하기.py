def solution(plans):
    answer = []
    stack=[]
    
    for i in range(len(plans)):
        name,start,play=plans[i]
        h,m=map(int,start.split(":"))
        seconds=h*3600+m*60
        play=int(play)*60
        plans[i]=[name,seconds,play]
    plans.sort(key=lambda x:x[1])
    
    
    for i in range(len(plans)):
        name,start,playtime=plans[i]
        
        if i<len(plans)-1:
            next_start=plans[i+1][1]
        else:
            answer.append(name)
            break
        
        remain_time=next_start-start
        #시간안에 끝내기 가능
        if remain_time>=playtime:
            answer.append(name)
            remain_time-=playtime
            
            while remain_time>0 and stack:
                last_name,last_remain=stack.pop()
                if remain_time>=last_remain:
                    remain_time-=last_remain
                    answer.append(last_name)
                else:
                    stack.append([last_name,last_remain-remain_time])
                    break
                
        
        #시간안에 끝내기 불가능
        else:
            stack.append([name,playtime-remain_time])
    while stack:
        name, _ = stack.pop()
        answer.append(name)
    return answer