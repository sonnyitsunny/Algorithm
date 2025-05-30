n = int(input())
count = 0

used_col = [False] * n           # 열 사용 여부
used_diag1 = [False] * (2 * n)   
used_diag2 = [False] * (2 * n)  

def dfs(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        d1 = row + col
        d2 = row - col + n - 1

        if used_col[col] or used_diag1[d1] or used_diag2[d2]:
            continue

        used_col[col] = True
        used_diag1[d1] = True
        used_diag2[d2] = True

        dfs(row + 1)

        used_col[col] = False
        used_diag1[d1] = False
        used_diag2[d2] = False

dfs(0)
print(count)
