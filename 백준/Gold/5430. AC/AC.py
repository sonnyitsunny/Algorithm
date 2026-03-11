from collections import Counter
from collections import deque

T = int(input())

for _ in range(T):
    command = input()
    n = int(input())
    before = input().strip()
    cnt = Counter(command)

    if n < cnt['D']:
        print("error")
        continue

    if n == 0:
        arr = []
    else:
        before_arr = list(before)
        before_arr.pop(0)
        before_arr.pop()
        after_arr = ''.join(before_arr)
        arr = after_arr.split(',')
        arr = list(map(int, arr))

    R_cnt = 0
    q = deque(arr)

    for com in command:
        if com == "R":
            R_cnt += 1
            continue

        if R_cnt % 2 == 0:
            q.popleft()
        else:
            q.pop()

    arr = list(q)

    if R_cnt % 2 == 0:
        print("[", end='')
        print(','.join(map(str, arr)), end='')
        print("]")
    else:
        arr.reverse()
        print("[", end='')
        print(','.join(map(str, arr)), end='')
        print("]")