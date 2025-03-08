n,m=map(int,(input().split()))

#딕셔너리로 확인하고, 값이 1인거를 리스트로 받기
dic={}

for _ in range(n):
    a=input()
    dic[a]=0

for _ in range(m):
    b=input()

    if b in dic:
        dic[b]=1

result=[k for k,v in dic.items() if v==1]
result.sort()

print(len(result))
for i in result:
    print(i)