n=int(input())
nums=list(map(int,input().split()))
nums.sort()
total=0
result=0
for num in nums:
    total+=num
    result+=total

print(result)