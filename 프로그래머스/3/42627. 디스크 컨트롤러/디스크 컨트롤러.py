import heapq
def solution(jobs):
    answer = 0
    result=[]
    arr=[]# 힙
    time=0
    count=0
    idx=0
    jobs.sort(key=lambda x:x[0])
        
    while count<len(jobs):
        while idx<len(jobs) and jobs[idx][0]<=time:
            heapq.heappush(arr,(jobs[idx][1],jobs[idx][0],idx))
            idx+=1
        if arr:
            spending,start,idk=heapq.heappop(arr)
            count+=1
            time+=spending
            result.append(time-start)
            
            
        else:
            time=jobs[idx][0]
        
        
        
    answer=sum(result)//len(result)
    
    
    
    
    return answer