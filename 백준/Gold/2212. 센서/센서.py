import sys
input = sys.stdin.readline

N=int(input())
K=int(input())

sensors=list(map(int,input().split()))
sensors.sort()

dist=[]
for i in range(N-1):
    dist.append(sensors[i+1]-sensors[i])

dist.sort(reverse=True)

print(sum(dist[K-1:]))