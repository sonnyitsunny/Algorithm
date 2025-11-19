import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_cnt = float('inf')
visited = [False] * n


visited[0] = True
path = [0]

def dfs(curr, depth, cost):
    global min_cnt


    if cost >= min_cnt:
        return

    if depth == n:
  
        if arr[curr][0] != 0:
            min_cnt = min(min_cnt, cost + arr[curr][0])
        return

    for next in range(1, n):  
        if not visited[next] and arr[curr][next] != 0:
            visited[next] = True
            dfs(next, depth + 1, cost + arr[curr][next])
            visited[next] = False

dfs(0, 1, 0)
print(min_cnt)
