import math


def gcd(array):
    result=array[0]
    
    for i in range(1,len(array)):
        result=math.gcd(result,array[i])
    return result

def check(x,array):
    for arr in array:
        if arr%x==0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    gcdA=gcd(arrayA)
    gcdB=gcd(arrayB)
    
    if check(gcdA,arrayB):
        answer=max(gcdA,answer)
    if check(gcdB,arrayA):
        answer=max(gcdB,answer)

    
    return answer