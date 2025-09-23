import sys
input = sys.stdin.readline
import heapq


n,m=map(int,input().split())
arr=list(map(int,input().split()))
heapq.heapify(arr)
#m번 만큼 반복문 돌림
#큐에 넣고
#최소 뽑고

#최소2 뽑고 
#둘이 더함 그리고 큐에 2번 넣음
for _ in range(m):
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    c=a+b
    heapq.heappush(arr,c)
    heapq.heappush(arr,c)

#합
print(sum(arr))





 
