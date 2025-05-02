from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)  # 1층부터 F층까지

def bfs(start):
    queue = deque()
    queue.append((start, 0))  # 현재 층, 버튼 누른 횟수
    visited[start] = True

    while queue:
        current, count = queue.popleft()
        if current == G:
            return count

        for next_floor in (current + U, current - D):
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                queue.append((next_floor, count + 1))

    return "use the stairs"

print(bfs(S))
