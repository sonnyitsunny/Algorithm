# from bisect import bisect_right
def solution(people, limit):
    answer=0
    i,j=0,len(people)-1
    people.sort()
    while i<=j:
        if people[i]+people[j]<=limit:
            i+=1
        j-=1
        answer+=1
            
                    
    return answer


# answer = 0
#     n=len(people)
#     people.sort()
#     visited=[False]*(n)
    
#     for i in range(n-1,-1,-1):
#         if not visited[i]:
#             weight=limit-people[i]
#             index=bisect_right(people,weight)
#             visited[i]=True
#             alone=True
#             for j in range(index-1,-1,-1):
#                 if not visited[j]:
#                     visited[j]=True
#                     answer+=1
#                     alone=False
#                     break
#             if alone:
#                 answer+=1