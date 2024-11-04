import sys
#input=sys.stdin.readline


n=int(input())
stack=[]
cur=1
temp=[]
safe=True

for _ in range(n):
    seq=int(input())
    while cur<=seq:
        temp.append(cur)
        cur+=1
        stack.append('+')
    
    if temp[-1]==seq:
        stack.append('-')
        temp.pop()

    else:
        safe=False
        break

if safe!=True:
    print('NO')
else:
    for i in stack:
        print(i)