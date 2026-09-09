def solution(answers):
    answer = []
    p1=[1, 2, 3, 4, 5]
    p2=[2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ps1=0
    ps2=0
    ps3=0
    n=len(answers)
    max_r=0
    for i in range(n):
        if answers[i]==p1[i%len(p1)]:
            ps1+=1
        if answers[i]==p2[i%len(p2)]:
            ps2+=1     
        if answers[i]==p3[i%len(p3)]:
            ps3+=1
    max_r=max(ps1,ps2,ps3)
    if max_r==0:
        return answer
    if ps1==max_r:
        answer.append(1)
    if ps2==max_r:
        answer.append(2)   
    if ps3==max_r:
        answer.append(3)
    answer.sort()
    return answer