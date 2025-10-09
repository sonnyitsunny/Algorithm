from itertools import permutations

def check(user,banned_id):
    for i in range(len(banned_id)):
        if len(user[i])!=len(banned_id[i]):
            return False
        
        for j in range(len(user[i])):
            if banned_id[i][j]=='*':
                continue
            if banned_id[i][j]!=user[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer=[]
    
    user_perm=permutations(user_id,len(banned_id))
    
    for user in user_perm:
        
        if not check(user,banned_id):
            continue
            
        else:
            user=set(user)
            if user not in answer:
                answer.append(user)
        
    return len(answer)