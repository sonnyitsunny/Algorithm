import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(start,arr):
    if len(arr)==6:
        print(*arr)
        return
    
    for i in range(start,k):
        dfs(i+1,arr+[nums[i]])



while True:
    nums=list(map(int,input().split()))
    if len(nums)==1:
        break
    k=nums.pop(0)


    dfs(0,[])

    print()
