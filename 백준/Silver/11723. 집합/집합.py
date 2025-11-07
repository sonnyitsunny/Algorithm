import sys

input=sys.stdin.readline

S=set()
M=int(input())



for _ in range(0,M):
    cal=(list(input().split()))
    a=cal[0]
    
    
    if len(cal)==1:
        if a=='all':
        
            for i in range(0,20):
                
                S.add(i+1)

        else:
            
            S=set()
        
        
    else:
        if a=='add':
            target = int(cal[1])
            if target not in S:
                S.add(target)

        elif a=='remove':
            target = int(cal[1])
            if target in S:
                S.remove(target)
        
        elif a=='check':
            target = int(cal[1])
            if target in S:
                print(1)
            else:
                print(0)
        
        elif a=='toggle':
            target = int(cal[1])
            if target in S:
                S.remove(target)
            else:
                S.add(target)

        
            

        
        
    