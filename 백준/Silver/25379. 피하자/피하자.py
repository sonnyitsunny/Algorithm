n=int(input())
arr=list(map(int,input().split()))


#왼쪽에 짝수놓기 오른쪽 홀수놓기
costA = 0

#왼쪽에 홀수 오른쪽 짝수
costB = 0

cnt1=0
cnt0=0

for v in arr:
    if v%2==0:
        costA+=cnt1
        cnt0+=1
    else:
        cnt1+=1
        costB+=cnt0


print(min(costA,costB))