import heapq

def change(time):
    hh,mm=map(int,time.split(":"))
    return hh*60+mm

def solution(book_time):
    answer = 0
    
    book_time.sort(key=lambda x:x[0])
    heap=[]
    
    for start,end in book_time:
        start=change(start)
        end=change(end)+10
        
        if heap and start>=heap[0]:
            heapq.heappop(heap)
        else:
            answer+=1
        heapq.heappush(heap,end)
    
    
    
    return answer