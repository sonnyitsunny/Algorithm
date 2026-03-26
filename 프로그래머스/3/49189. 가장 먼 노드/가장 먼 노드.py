import heapq

def solution(n, edge):
    answer = 0
    
    graph=[[] for _ in range(n+1)]
    for s,e in edge:
        graph[s].append((e,1))
        graph[e].append((s,1))
    
    INF=int(1e9)
    distance=[INF]*(n+1)
    
    def dijkstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0
        
        while q:
            dist,now = heapq.heappop(q)
            if distance[now]<dist:
                continue
            for neighbor,cost in graph[now]:
                new_cost=dist+cost
                if new_cost<distance[neighbor]:
                    distance[neighbor]=new_cost
                    heapq.heappush(q,(new_cost,neighbor))
    
    
    
    dijkstra(1)
    max_v=max(distance[1:])
    answer=distance.count(max_v)
    return answer