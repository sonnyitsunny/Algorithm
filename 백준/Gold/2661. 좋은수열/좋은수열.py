import sys
input = sys.stdin.readline

N=int(input())


def check(s):
    length=len(s)
    for i in range(1,length//2+1):
        if s[-i:]==s[-2*i:-i]:
            return False
    return True


def dfs(num):
    
    if N==len(num):
        print(num)
        exit()


    for i in (1,2,3):
        
        if check(num+str(i)):
            dfs(num+str(i))



dfs("")