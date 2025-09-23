import sys
input = sys.stdin.readline

N=int(input())

zero=0
one=0
minus=[]
plus=[]

for _ in range(N):
    num=int(input())

    if num>1:
        plus.append(num)
    elif num<0:
        minus.append(num)
    elif num==1:
        one+=1
    else:
        zero+=1
        

minus.sort()
plus.sort(reverse=True)
total=0


for i in range(0,len(plus)-1,2):
    total+=plus[i]*plus[i+1]
if len(plus)%2==1:
    total+=plus[-1]

total += one

for i in range(0,len(minus)-1,2):
    total+=minus[i]*minus[i+1]
if len(minus)%2==1:
    if zero==0:
        total+=minus[-1]
print(total)