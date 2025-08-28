import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


#선택한 애를 기준으로 얘보다 작은애가 몇개 있는지 알아야함 근데 서로 달라야함

N=int(input())

arr=list(map(int,input().split()))

#중복 제거
target=list(set(arr))
target.sort()
result=[]


for num in arr:
    
    j=bisect_right(target,num)
    #자기자신 빼기
    result.append(j-1)
print(*result)