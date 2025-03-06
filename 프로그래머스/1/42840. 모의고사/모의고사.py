def solution(answers):
    answer = []
    #방식세팅 후 answer 반복문 돌리기하고 방식이랑 비교 % 연산자 이용
    #같으면 cnt1, cnt2, cnt3 추가
    
    dic={'cnt1':0,'cnt2':0,'cnt3':0}
    
    p1=[1,2,3,4,5] # %5
    p2=[2, 1, 2, 3, 2, 4, 2, 5] # %8
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # %10
    
    for i in range(0,len(answers)):
        if p1[i%5]==answers[i]:
            dic['cnt1']+=1
        if p2[i%8]==answers[i]:
            dic['cnt2']+=1
        if p3[i%10]==answers[i]:
            dic['cnt3']+=1
    max_key=max(dic['cnt1'],dic['cnt2'],dic['cnt3'])
    
    result=[k for k,v in dic.items() if v==max_key]
    for i in result:
        if i=='cnt1':
            answer.append(1)
        if i=='cnt2':
            answer.append(2)
        if i=='cnt3':
            answer.append(3)
            
    answer.sort()
    return answer