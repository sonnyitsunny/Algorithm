

def solution(n, computers):
    answer = 0
    visited=[0]*n
    
    def dfs(start):
        visited[start]=1
        for i in range(n):
            if start!=i and computers[start][i]==1 and not visited[i]:
                dfs(i)


    
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            answer+=1
    
    return answer