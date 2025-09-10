

def solution(n):
    answer = float('inf')
    
    nxt=n+1
    
    
    while True:
        b_nxt=bin(nxt)[2:]
        b_n=bin(n)[2:]
        
        if b_nxt.count("1") == b_n.count("1"):
            answer=int(b_nxt,2)
            break
        nxt+=1
    
    return answer