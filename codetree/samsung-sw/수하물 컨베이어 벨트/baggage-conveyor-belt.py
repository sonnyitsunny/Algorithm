
from collections import defaultdict, deque

N = int(input())
board = []

answer = []

for _ in range(N):
    board.append(list(map(int, input().split())))

B = int(input())
result = [0] * B

waiting = defaultdict(list)

for i in range(1, B + 1):
    arr = list(map(int, input().split()))
    waiting[arr[0]].append([i] + arr[1:])

turn = 1

broken = [False] * B

q = deque()
q_wait = deque()

visited = [[False] * N for _ in range(N)]

# 1 아래, 2 왼쪽, 3 위, 4 오른쪽
direction = {
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
    4: (0, 1)
}

while len(answer) != B:

    # 무게 내림차순, 번호 오름차순
    q = deque(sorted(q, key=lambda x: (-x[2], x[0])))

    # -------------------------
    # 1. 수하물 이동
    # -------------------------

    # 현재 수하물들이 차지한 위치
    occupied = {}

    for num, t, w, cnt, r, c in q:
        occupied[(r, c)] = num

    # 목적지별 우선권을 가진 수하물
    target = {}

    for num, t, w, cnt, r, c in q:

        d = board[r][c]

        if d not in direction:
            continue

        dr, dc = direction[d]
        nr = r + dr
        nc = c + dc

        # 격자 범위 및 벽 확인
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if board[nr][nc] == 0:
            continue

        # 이미 정렬했으므로 최초 수하물이 우선
        if (nr, nc) not in target:
            target[(nr, nc)] = num

    # 수하물 번호 -> 이동 목적지
    dest = {}

    for pos, num in target.items():
        dest[num] = pos

    # 이동 우선권을 가진 수하물
    winners = set(dest)

    # 우선권이 없어 이동할 수 없는 수하물
    blocked = set()

    for bag in q:
        if bag[0] not in winners:
            blocked.add(bag[0])

    # 다른 수하물이 움직여야만 이동할 수 있는 관계
    depend = defaultdict(list)

    for num, pos in dest.items():
        other = occupied.get(pos)

        if other is not None:
            depend[other].append(num)

    # 이동 불가능 상태를 뒤쪽 수하물로 전파
    dq = deque(blocked)

    while dq:
        cur = dq.popleft()

        for nxt in depend[cur]:
            if nxt not in blocked:
                blocked.add(nxt)
                dq.append(nxt)

    moved = winners - blocked

    # -------------------------
    # 2. 실제 이동 및 적재·파손
    # -------------------------

    next_q = deque()

    for num, t, w, cnt, r, c in q:

        if num in moved:
            r, c = dest[num]
            cnt = 0
        else:
            cnt += 1

        # 3턴 연속 이동 실패 시 파손
        if cnt >= 3:
            broken[num - 1] = True

        # 적재 장소 도착
        if board[r][c] == 9:
            if broken[num - 1]:
                result[num - 1] = -turn
            else:
                result[num - 1] = turn

            answer.append(num)
        else:
            next_q.append((num, t, w, cnt, r, c))

    q = next_q

    # 이동 후 점유 상태 다시 생성
    visited = [[False] * N for _ in range(N)]

    for num, t, w, cnt, r, c in q:
        visited[r][c] = True

    # -------------------------
    # 3. 새로운 수하물 투입
    # -------------------------

    # 이번 턴 투입 예정인 수하물을 대기열에 추가
    for bag in waiting[turn]:
        q_wait.append(bag)

    # 대기열에 있는 수하물 투입 시도
    for _ in range(len(q_wait)):

        num, r, c, w = q_wait.popleft()

        r -= 1
        c -= 1

        if not visited[r][c]:

            
            visited[r][c] = True

            # 번호, 이동 시작 턴, 무게,
            # 연속 이동 실패 횟수, 행, 열
            q.append((num, turn + 1, w, 0, r, c))

        else:
            # 이번 턴에 투입하지 못하면 계속 대기
            q_wait.append((num, r + 1, c + 1, w))

    turn += 1

print(*result)
