from collections import defaultdict

def solution(points, routes):
    answer = 0
    accident=defaultdict(int)
    
    
    for route in routes:
        t=0
        #하나의 4->3->2 로 이동한다면 시작4 목표3   시작3 목표2 이런 식으로 반복
        for i in range(len(route)-1): 
            sr,sc=points[route[i]-1] #시작
            er,ec=points[route[i+1]-1] #목표
            
            
            if er<sr:
                step=-1
            else:
                step=1
                
            for r in range(sr,er,step): #r우선 맞추고
                accident[(r,sc,t)]+=1
                if accident[(r,sc,t)]==2:
                    answer+=1
                t+=1
            
            if ec<sc:
                step=-1
            else:
                step=1
            for c in range(sc,ec,step): #c맞춘다
                accident[(er,c,t)]+=1
                if accident[(er,c,t)]==2:
                    answer+=1
                t+=1
            
            #도착점
            if i == len(route)-2:
                accident[(er,ec,t)]+=1

                if accident[(er,ec,t)]==2:
                    answer+=1
                
    
    return answer