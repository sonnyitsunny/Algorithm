
from itertools import combinations
def solution(n, q, ans):
    answer = []
    m=len(q)
    for com in combinations(range(1,n+1),5):
        com=set(com)
        #q수만큼 반복해서 비교하기 모든 조건 만족하면 answer추가
        check=True
        for i in range(m):
            target=set(q[i])
            if len(target&com)!=(ans[i]):
                check=False
                break

        if check:
            answer.append(com)
            
    
    return len(answer)