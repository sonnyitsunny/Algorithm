t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        input()  # 비행편 정보는 안 써도 됨
    print(n - 1)