from collections import defaultdict

n=int(input())
dic=defaultdict(int)

arr=list(input().split())
for c in arr:

    if "Cheese" == c[-6:]:
        dic[c]=1
    
if len(dic)>=4:
    print("yummy")
else:
    print("sad")