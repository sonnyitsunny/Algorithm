
def solution(numbers):
    answer = ''
    result=list(map(str,numbers))
    
    result.sort(key=lambda x:x*3,reverse=True)
    
    answer=answer.join(result)
    
    
    return str(int(answer))