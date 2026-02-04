N,M=map(int,input().split())
cnt=0
if N>0:
    books=list(map(int,input().split()))
    books.reverse()
    cnt=1

bag=0 # 현재 가방에 든 무게


while N>0:
    
    if books[-1]+bag>M:
        bag=0
        cnt+=1
        continue
    
    bag+=books[-1]
    books.pop()
    N-=1


print(cnt)