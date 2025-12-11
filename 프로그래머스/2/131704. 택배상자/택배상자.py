def solution(order):
    answer = 0
    
    stack=[]
    con=sorted(order)
    i=0
    
    for c in con:
        if c==order[i]:
            i+=1
            answer+=1
            
            while stack and stack[-1] == order[i]:
                stack.pop()
                answer += 1
                i += 1
        else:
            stack.append(c)
            
            
    while stack and stack[-1] == order[i]:
        stack.pop()
        answer += 1
        i += 1
    
    return answer