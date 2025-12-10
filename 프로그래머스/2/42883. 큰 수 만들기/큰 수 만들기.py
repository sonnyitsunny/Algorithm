def solution(number, k):
    answer = ''
    
    stack=[]
    for num in number:
        
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k-=1
        stack.append(num)
    
    for _ in range(k):
        stack.pop()
    
    
    
    answer=''.join(stack)
    
    
    return answer