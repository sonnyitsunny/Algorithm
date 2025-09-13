
def solution(players, m, k):
    
    answer = 0 #증설 횟수
    server_list=[]
    now_serve=0
    
    for player in players:


        
        if (now_serve+1)*m<=player:#현재서버로 커버 못하는경우
            users=player-(now_serve+1)*m # 이용못하고 있는 사람 구하기
            
            if users%m==0:
                add_server=users//m
                add_server+=1
            else:
                add_server=users//m
                add_server+=1
            
            answer+=add_server #증설횟수 추가
            
            for _ in range(add_server):#서버반영
                server_list.append(k)
            
        #
        for i in range(len(server_list)):
            server_list[i]-=1 #서버 수명 줄이기
        dead_servers=0
            
        for i in range(len(server_list)):#현재 가동중인 서버 개수 구하기
            if server_list[i]<=0:
                dead_servers+=1
        now_serve=len(server_list)-dead_servers #현재 서버 개수
            
    
    return answer