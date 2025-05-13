#n받고 

#음수다 그러면
# 양수를 집어넣을 떄는 -붙이고 꺼낼 때도 -붙여서 
# 음수를 집어넣을 때는 그냥 넣고 꺼낼때도 그냥 꺼내?




import sys
import heapq
input=sys.stdin.readline

n=int(input())

heap=[]

for _ in range(n):
    row=list(map(int,input().split()))

    for num in row:
        heapq.heappush(heap,num)
        if n<len(heap):
            heapq.heappop(heap)
print(heapq.heappop(heap))