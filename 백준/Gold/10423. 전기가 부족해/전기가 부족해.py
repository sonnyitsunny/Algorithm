import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a



N, M, K = map(int, input().split())
plants = list(map(int, input().split()))
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [i for i in range(N + 1)]

first_plant = plants[0]
for i in range(1, K):
    union(first_plant, plants[i])

edges.sort()
res = 0
for cost, a, b in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    res += cost
print(res)