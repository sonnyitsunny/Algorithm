def solution(n):
    answer = 0
    
    
    arr=[]
    
    def dfs():
        nonlocal answer
        if len(arr)==n:
            answer+=1
            return
        
        row=len(arr)
        for col in range(n):
            possible=True
            #같은행 같은열
            for r,c in enumerate(arr):
                if c==col:
                    possible=False
                    break
                    #대각선
                if abs(r-row) == abs(c-col):
                    possible=False
                    break
            
            if possible:
                arr.append(col)
                dfs()
                arr.pop()
                
        return answer
        
    
    
    
    dfs()
    
    return answer