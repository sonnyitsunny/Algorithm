

N1,N2=map(int,input().split())
arr1=list(input())
arr2=list(input())
arr1.reverse()
T=int(input())

line=[]

for a1 in arr1:
    line.append((1,a1))
for a2 in arr2:
    line.append((-1,a2))

length=len(line)

start=0 # 시작 지점

for _ in range(T):
    for i in range(length-1):
        if start<=i and line[i][0]==1 and line[i+1][0]==-1:
            line[i],line[i+1]=line[i+1],line[i]
            start=i+2

    start=0
res=[]
for dir, name in line:
    res.append(name)
print(''.join(res))