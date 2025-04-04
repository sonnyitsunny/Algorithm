n = int(input())
arr = list(map(int, input().split()))

# 1. 증가 수열
dp_inc = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)

# 2. 감소 수열
dp_dec = [1]*n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)

# 3. 최대 바이토닉 길이
max_len = 0
for i in range(n):
    max_len = max(max_len, dp_inc[i] + dp_dec[i] - 1)

print(max_len)
