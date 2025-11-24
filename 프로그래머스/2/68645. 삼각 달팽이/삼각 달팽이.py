def solution(n):
    answer = []
    tri=[[0]*n for _ in range(n)]
    x=-1
    y=0
    num=1
    
    
    for step in range(n):
        for _ in range(step,n):
            if step%3==0:
                x+=1
            elif step%3==1:
                y+=1
            else:
                x-=1
                y-=1
            
            tri[x][y]=num
            num+=1
    for i in range(n):
        for j in range(i+1):
            answer.append(tri[i][j])
    
    
    
    
    return answer