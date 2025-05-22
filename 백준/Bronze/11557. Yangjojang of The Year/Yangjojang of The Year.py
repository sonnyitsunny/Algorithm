n=int(input())


for _ in range(n):
    k=int(input())
    arr=[]
    for _ in range(k):
    
        a,b=input().split()
        arr.append((a,int(b)))
    arr.sort(key=lambda x:-x[1])
    print(arr[0][0])