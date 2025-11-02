def solution(want, number, discount):
    answer = 0
    
    n=len(discount)
    for i in range(n-9):
        targets=discount[i:i+10]
        #print(targets)
        match=True
        
        for j in range(len(want)):
            if targets.count(want[j])!=number[j]:
                match=False
                break
                
        if match:
            answer+=1
            
            
            
            
                
    return answer