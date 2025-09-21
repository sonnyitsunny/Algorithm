import sys
input = sys.stdin.readline

N = int(input())
arr=[False,False]+ [True]*(N+1)
prime=[]

for i in range(2,N+1):
    if arr[i]:
        prime.append(i)
        for j in range(2*i,N+1,i):
            arr[j]=False

ans=0

left=0
right=0
total=0

while True:
    
    if total>=N:
        if total==N:
            ans+=1
        total-=prime[left]
        left+=1
    
    elif right==len(prime):
        break

    else:
        total+=prime[right]
        right+=1

print(ans)