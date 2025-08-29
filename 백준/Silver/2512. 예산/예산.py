import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right


N=int(input())
nums=list(map(int,input().split()))
nums.sort()
M=int(input())

if sum(nums)<=M:
    print(nums[-1])
else:
    left,right=0,max(nums)
    ans=0
    while left<=right:
        mid=(left+right)//2
        s=0
        for x in nums:
            if x<=mid:
                s+=x
            else:
                s+=mid
            
        if s<=M:
            ans=mid
            left=mid+1
        else:
            right=mid-1
    print(ans)