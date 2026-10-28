from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    cnt=defaultdict(int)
    #orders를 하나씩가져옴
    for order in orders:
        
        #course 를 하나씩 가져옴
        for cour in course:
            
            #courese보다 order길이가 크거나 같은지 확인
            if len(order)>=cour:
                #되면 arr=com(order,order)
                arr=list(combinations(sorted(order),cour))
                for a in arr:
                    cnt[a]+=1
                    
            #안되면 컨티뉴
            else:
                continue
    #각 cour 별로 최대인 것들 cnt에서 찾기
    course_max=set()
    
    for cour in course:
        max_cnt=0
        for k,v in cnt.items():
            if cour==len(k) and v>=2:
                max_cnt=max(max_cnt,v)
        course_max.add((cour,max_cnt))
    
    for c,max_cnt in course_max:
        for k,v in cnt.items():
            menu=""
            if len(k)==c and v==max_cnt:
                
                sort_k=sorted(k,key=lambda x:x[0])
                for s in sort_k:
                    menu+=s
                answer.append(menu)
    answer.sort()
    return answer