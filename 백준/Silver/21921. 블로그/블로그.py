import sys
#input=sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque




N,X=map(int,input().split())
visit=list(map(int,input().split()))



def max_sum1(visit,X):
    count=1
    window=sum(visit[:X])
    max_sum=window

    for i in range(X,len(visit)):
        window+=visit[i]-visit[i-X]
        
        
        if window>max_sum:
            count=1
            max_sum=max(max_sum,window)
        
        elif window==max_sum:
            count+=1
    
    return max_sum,count

m,c=max_sum1(visit,X)


if m==0:
    print('SAD')
else:
    print(m)
    print(c)


    #5에 2라면  0~1인덱스까지합구하기   x가 2, i가 2일때          +[2]-[0] 그러면 1~2까지 
    # x가 2 i가 3일떄 +[3]-[1] 그러면 2~3까지 i가 +[4]-[2] 3~4까지 