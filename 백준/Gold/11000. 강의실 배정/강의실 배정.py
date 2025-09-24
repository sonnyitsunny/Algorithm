import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: x[0])


heap = []
heapq.heappush(heap, times[0][1])  

for i in range(1, n):
    start, end = times[i]
    
    if heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))
