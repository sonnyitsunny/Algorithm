import sys
input=sys.stdin.readline

nums=list(map(int,(input().strip().split(":"))))


a=nums[0]
b=nums[1]
if a>=b:
    k=b
else:
    k=a
div=1

for i in range(k,0,-1):
    if a%i==0 and b%i==0:
        div=i
        break
a=a//div
b=b//div
print(str(a)+':'+str(b))