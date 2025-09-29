def solution(n, w, num):
    answer = 0
    
    height=n//w + 1
    
    box=[[0]*w for _ in range(height)]
    
    x=0
    y=0
    
    tmp=1
    floor=1
    
    for i in range(height-1,-1,-1):
        
        if floor%2==1 and tmp<=n:
            for j in range(w):
                if tmp<=n:
                    box[i][j]=tmp
                    if tmp==num:
                        x=i
                        y=j
                    tmp+=1
            floor+=1
        #역방
        else:
            if tmp<=n:
                for j in range(w-1,-1,-1):
                    if tmp<=n:
                        box[i][j]=tmp
                        if tmp==num:
                            x=i
                            y=j
                        tmp+=1
                floor+=1
    print(box)
    print(x,y)
    for i in range(x+1):
        if box[i][y]!=0:
            answer+=1
    
    return answer