
    


def solution(s):
    answer = []
    trans_cnt=0
    zero_cnt=0
    

    
    while len(s)!=1:
        tmp=""
        for i in s:
            if i=="1":
                tmp+=i
        
        trans_cnt+=1
        zero_cnt+=len(s)-len(tmp)
        
        n=len(tmp)
        tmp=bin(n)[2:]
        s=tmp
        
        
    
    answer=[trans_cnt,zero_cnt]
    
    return answer