def solution(participant, completion):
    answer = ''
    dic={}
    
    #해시에 다 넣고 1로 설정, 동명이면 +1
    #com돌면서 해시 -1해줌 그리고 거기서 0이 아닌 애를 찾아서 걔이름을 리턴해주면 됨
    
    for i in participant:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
            
    for j in completion:
        if j in dic:
            dic[j]-=1
    for k in dic:
        if dic[k]!=0:
            answer=k
        
        
        
    return answer