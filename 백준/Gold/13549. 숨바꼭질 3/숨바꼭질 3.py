from collections import deque

n, k = map(int, input().split())
MAX = 100001
dist = [-1] * MAX

q = deque()
q.append(n)
dist[n] = 0

while q:
    cur = q.popleft()

    if cur == k:
        print(dist[cur])
        break

    # 순간이동 (0초)
    if 0 <= cur * 2 < MAX and dist[cur * 2] == -1:
        dist[cur * 2] = dist[cur]
        q.appendleft(cur * 2)

    # 뒤로 걷기 (1초)
    if 0 <= cur - 1 < MAX and dist[cur - 1] == -1:
        dist[cur - 1] = dist[cur] + 1
        q.append(cur - 1)

    # 앞으로 걷기 (1초)
    if 0 <= cur + 1 < MAX and dist[cur + 1] == -1:
        dist[cur + 1] = dist[cur] + 1
        q.append(cur + 1)
