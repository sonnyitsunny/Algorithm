import sys
input = sys.stdin.readline
from collections import Counter


r,c,k=map(int,input().split())
A=[]
for _ in range(3):
    A.append(list(map(int,input().split())))

def rmath():
    
    #r연산
    for i in range(len(A)):
        new_row=[]
        d=Counter(A[i])
        del d[0]
        res=sorted(d.items(),key=lambda x:(x[1],x[0]))

        for v,c in res:
            new_row.append(v)
            new_row.append(c)
        A[i]=new_row
    
    #0추가
    length=0
    for row in A:
        length=max(len(row),length)

    for i in range(len(A)):
        cnt=length-len(A[i])
        for _ in range(cnt):
            A[i].append(0)

def rotate(A):
    trans=[]

    for j in range(len(A[0])):
        new_row=[]
        for i in range(len(A)):
            new_row.append(A[i][j])
        trans.append(new_row)

    return trans

limit=False
time=0
while time<=100:
    row=len(A)
    col=len(A[0])
    if 0<=r-1<row and 0<=c-1<col and A[r-1][c-1]==k:
        limit=True
        print(time)
        break
    
    
    

    if row>=col:
        #r연산
        rmath()
    else:
        
        #전치
        A=rotate(A)
        rmath()
        A=rotate(A)

    time+=1

if not limit:
    print(-1)


13
13
13