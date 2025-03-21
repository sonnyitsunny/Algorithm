import sys
input = sys.stdin.readline

info = []
N = int(input())
for i in range(N):
    age, name = input().split()
    info.append((i, int(age), name))  # 나이를 숫자로 바꿔서 저장

info.sort(key=lambda x: (x[1], x[0]))  # 나이 → 가입순 정렬

for person in info:
    print(person[1], person[2])
