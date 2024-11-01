def solution(diffs, times, limit):
    left=1
    right=max(diffs)
    
    answer = right
    
    while left<=right:
        total_time=times[0]
        level=(left+right)//2
        
        
        for i in range(1,len(diffs)):
            cur_diff=diffs[i]
            cur_time=times[i]
            prev_time=times[i-1]
            
            if cur_diff>level:
                total_time+=(prev_time+cur_time)*(cur_diff-level)+cur_time
            else:
                total_time+=cur_time
                
                
        #해당 레벨로 안되는 경우(리밋보다 total_time이 큰경우)        
        if total_time>limit:
            #level+=1 
            
            left=level+1
            
         #해당레벨로 리밋보다 작을경우
        else:
            answer=level
            right=level-1
            
    return answer
  