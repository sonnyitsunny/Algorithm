# 효과 실행 -> 점수 얻기 -> 시간 흐름
#시작할 떄로부터 240 초과한 경우 , 주사위 굴리기 전에 게임 종료
#시작할 때 기준 주사위 한번 굴리면 1점 얻고 매턴 시간이 4씩 흐름



prize1=0 #  35<= x <65
prize2=0 #  65<= x  <95
prize3=0 #  95<= x <125
prize4=0 # 125<=x  

# 새로운 게임을 시작할 때 점수가 0점으로 초기화
#  게임이 종료되지 않은 경우 그 당시 점수에 상관없이 보상을 받을 수 없다.

time=0
score=0


N=int(input())
arr=list(map(int,input().split()))
delta_point = 1 
delta_time = 4 

# 종료
def end():
    
    global prize1,prize2,prize3,prize4
    global time, score, delta_point, delta_time
    if 35<=score<65:
        prize1+=1
    elif 65<=score<95:
        prize2+=1
    elif 95<=score<125:
        prize3+=1
    elif score>=125:
        prize4+=1
    time=0
    score=0
    delta_point=1
    delta_time=4

for a in arr:
    
    if time>240:
        end()
        


    if a==1:
        end()
       

    elif a==2:
        if delta_point>1:
            delta_point=delta_point//2
        else:
            delta_time += 2
        score+=delta_point
        time+=delta_time
            

    elif a==3:
        
        score+=delta_point
        time+=delta_time

    elif a==4:
        time+=56
        score+=delta_point
        time+=delta_time
    
    elif a==5:
        if delta_time>1:
             delta_time -= 1
        score+=delta_point
        time+=delta_time
    
    elif a==6:
        if delta_point<32:
            delta_point*=2
        score+=delta_point
        time+=delta_time



print(prize1)
print(prize2)
print(prize3)
print(prize4)

