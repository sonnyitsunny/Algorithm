import sys
input = sys.stdin.readline
from bisect import bisect_left


P=int(input())

for _ in range(P):
    arr=list(map(int,input().split()))
    case_num=arr.pop(0)
    n=len(arr)
    
    back_move=0

    for i in range(1,n):
        t=bisect_left(arr[:i],arr[i])
        if len(arr[:i]) == t:
            continue
        else:
            tmp=arr.pop(i)
            
            arr.insert(t,tmp)
            back_move+=i-t
    print(case_num,back_move)