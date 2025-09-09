def solution(s):
    answer = False
    
    #(의 갯수
    cnt=0
    
    for i in s:
        if i=="(":
            if cnt>=0:
                cnt+=1
                answer=True
            else:
                return False
            
        # ")" 인 경우
        else:
            if cnt>=1:
                cnt-=1
                answer=True
            else:
                return False
    if cnt!=0:
        return False
    

    return True