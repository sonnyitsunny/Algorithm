import sys
input = sys.stdin.readline
from collections import defaultdict

N,M=map(int,input().split())

idol=defaultdict(list)

for _ in range(N):
    group=input().strip()
    nums=int(input())

    for _ in range(nums):
        name=input().strip()
        idol[group].append(name)


for _ in range(M):
    name=input().strip()
    case=int(input())
    
    #팀이름 출력
    if case==1:
        for (k,v) in idol.items():
            if name in v:
                print(k)
                

    #속한 멤버 이름을 사전순으로 한줄에 한명씩 출력
    else:
        result=sorted(idol[name])
        for name in result:
            print(name)