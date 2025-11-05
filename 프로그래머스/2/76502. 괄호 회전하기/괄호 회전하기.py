
def check(target):
    pair={"]":"[","}":"{",")":"("}
    
    stack=[]
    for t in target:
        if t in "[{(":
            stack.append(t)
        else:
            if not stack or stack[-1]!=pair[t]:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True

def solution(s):
    answer = 0
    n=len(s)
    for i in range(n):
        target=s[i:]+s[:i]
        if check(target):
            answer+=1
    
    return answer