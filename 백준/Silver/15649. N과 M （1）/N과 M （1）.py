from itertools import permutations

N, M = map(int, input().split())

# N까지의 숫자에서 길이 M의 순열을 생성
result = list(permutations(range(1, N + 1), M))

# 각 순열을 공백으로 구분된 형식으로 출력
for perm in result:
    print(' '.join(map(str, perm)))
