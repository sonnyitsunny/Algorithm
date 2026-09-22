def solution(people, limit):
    answer = 0
    n=len(people)
    people.sort()
    left=0
    right=n-1
    
    while left<=right:
        #tmp는 남은 kg
        tmp=limit-people[right]
        
        if people[left]<=tmp:
            answer+=1
            left+=1
            right-=1
        else:
            answer+=1
            right-=1
    
    return answer