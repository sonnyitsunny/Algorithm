n, m = map(int, input().split())

arr = []


for i in range(n):
    arr.append(list(input()))
cnt, other = 0, 0
result = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'C':
            c += 1
    if max(a,c,g,t) == a:
        result += 'A'
        other += c + g +t
    elif max(a,c,g,t) == c:
        result += 'C'
        other += a + g +t
    elif max(a,c,g,t) == g:
        result += 'G'
        other += a + c +t
    elif max(a,c,g,t) == t:
        result += 'T'
        other += c + g + a
    
print(result)
print(other)
