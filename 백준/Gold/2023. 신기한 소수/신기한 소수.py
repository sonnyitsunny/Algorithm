import sys
input = sys.stdin.readline
import math
N=int(input())
res=[]



def isPrime(new):
    int_new=int(new)
    if int_new<2:
        return False
    for i in range(2,int(int_new**0.5)+1):
        if int_new%i==0:
            return False
    return True






def dfs(nums,depth):
    if depth==N:
        
        res.append(int(nums))


    for i in range(1,10):
        new=nums+str(i)
        if isPrime(new):
        
            dfs(nums+str(i),depth+1)




dfs("",0)
res.sort()
for r in res:
    print(r)