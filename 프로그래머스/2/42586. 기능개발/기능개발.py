def solution(progresses, speeds):
    answer = []
    n=len(progresses)
    stack=[]
    for i in range(n):
        p=progresses[i]
        s=speeds[i]
        
        for day in range(1,100):
            if p+s*day>=100:
                stack.append(day)
                break
    
    prev=stack[0]
    cnt=1
    for i in range(1,n):
        if prev>=stack[i]:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
            prev=stack[i]
    answer.append(cnt)
            
    return answer