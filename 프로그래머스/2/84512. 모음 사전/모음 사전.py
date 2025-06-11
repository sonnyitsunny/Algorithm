def solution(word):
    answer = 0
    
    dic=[ 'A', 'E', 'I', 'O', 'U']
    
    words=[]
    
    
    def dfs(current):
        if len(current)>5:
            return
        if current:
            words.append(current)
        
        for d in dic:
            dfs(current+d)
    
    dfs("")
    answer=words.index(word)+1
    return answer