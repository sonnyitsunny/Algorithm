import heapq
def solution(operations):
    answer = [0,0]
    
    max_q=[]
    min_q=[]
    holding=set()
    
    for op in operations:
        com,str_num=op.split()
        num=int(str_num)
        #삽입
        if com=="I":
            if num!=0:
                holding.add(num)
                heapq.heappush(min_q,num)
                heapq.heappush(max_q,-num)
            else:
                holding.add(num)
                heapq.heappush(min_q,num)
                heapq.heappush(max_q,num)
        #삭제
        else:
            #최대값제거
            if num==1 and max_q:
                while max_q:
                    t=-heapq.heappop(max_q)
                    if t in holding:
                        holding.remove(t)
                        break
                    
            
            #최소 값 제거
            elif num==-1 and min_q:
                while min_q:
                    t=heapq.heappop(min_q)
                    if t in holding:
                        holding.remove(t)
                        break
    min_c=False
    max_c=False
    while min_q and max_q:
        t=-heapq.heappop(max_q)
        if t in holding and answer[0]==0 and not max_c:
            answer[0]=t
            max_c=True
        else:
            pass
        
        t=heapq.heappop(min_q)
        if t in holding and answer[1]==0 and not min_c:
            answer[1]=t
            min_c=True
        else:
            pass
    return answer