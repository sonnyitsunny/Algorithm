
N,K=map(int,input().split())

result=list(map(int,input().split(',')))
temp=[]


for _ in range(K):
    for i in range(N-1):
        temp.append(result[i+1]-result[i])

    result=temp
    temp=[]
    N-=1


print(','.join(map(str,result)))
