from itertools import permutations

def isPrime(num):
    
    if num<=1:
        
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def solution(numbers):
    answer = 0

    nums=list(numbers)
    n=len(nums)
    target=[]
    
    for i in range(1,n+1):
        result=list(permutations(nums,i))
        for j in result:
            word=''
            for k in j:
                word+=k
            target.append(int(word))
    target=set(target)
    for t in target:
        print(t)
        if isPrime(t):
            answer+=1

        

    return answer