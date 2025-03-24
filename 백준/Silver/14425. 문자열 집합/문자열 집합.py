#N M 받아
#N에 들어오는 거 해시에 넣음
#M에 들어오는거 해시랑 비교해서 변수에 +1해주기

hash={}
N,M=map(int,input().split())
cnt=0
for _ in range(N):
    word=input()
    hash[word]=0


for _ in range(M):
    word=input()

    if word in hash:
        cnt+=1

print(cnt)