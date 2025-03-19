from collections import deque
import sys
sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

number=list(input().split('-'))

result=0


#첫그룹
if '+' in number[0]:
        
        st_nums=list(number[0].split('+'))
        in_nums=list(map(int, st_nums))
        x=sum(in_nums)
        result+=x


else:
        x=int(number[0])
        result+=x


#그이후

for i in number[1:]:
    if '+' in i:
        st_nums=list(i.split('+'))
        in_nums=list(map(int, st_nums))
        x=sum(in_nums)
        result-=x


    else:
        x=int(i)
        result-=x
print(result)