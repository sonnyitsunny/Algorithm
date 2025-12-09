import sys
input = sys.stdin.readline

N = int(input())

res=[]
def dfs(num):
    res.append(num)
    last=num%10

    for next_digit in range(0,last):
        dfs(num*10+next_digit)

for i in range(10):
    dfs(i)

res.sort()
if N>=len(res):
    print(-1)
else:
    print(res[N])