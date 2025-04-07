A, B = input().split()
min_diff = len(A)

for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            count += 1
    min_diff = min(min_diff, count)

print(min_diff)
