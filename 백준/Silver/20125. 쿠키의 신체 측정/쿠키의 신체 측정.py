import sys
input = sys.stdin.readline


#각각 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이를 공백으로 구분해서 출력
# *는 쿠키의 신체 부분이고, _ 는 쿠키의 신체가 올라가 있지 않은 칸

N=int(input())

head_check=False
head_x=0
head_y=0

result=[]

maps=[]
for i in range(N):
    row=list(input().strip())
    if not head_check and "*" in row:
        head_x=i
        head_y=row.index("*")
        head_check=True
    maps.append(row)

#왼팔길이 구하는 방법
#head_x + 1 행의 리스트에서  head_y-row.index("*")
row=maps[head_x + 1]
result.append(head_y-row.index("*"))


#오른팔
#head_x+1q,head_y를 시작으로 head_y+1부터 _만날때까지 혹은 범위 끝
tmp=0
for i in range(N-1,-1,-1):
    if row[i]=="*":
        tmp=i
        break
result.append(tmp-head_y)


#허리는 head_x+1부터 열은 같은 head_y로 하고 몇개나 있는지 _만날떄까지
core=0
for i in range(head_x+2,N):
    if maps[i][head_y] == "*":
        core+=1
    else:
        break
result.append(core)


#허리구 하고
#왼다리 head_x+1 에다가 허리 길이 더하고, head_y-1부터 밑으로 _만날 때까지 혹은 끝날때까지
left_leg=0
for i in range(head_x+2+core,N):
    if maps[i][head_y-1]=="*":
        left_leg+=1

result.append(left_leg)


#오른 다리   head_x+1 에다가 허리 길이 더하고, head_y+1부터 밑으로 _만날 때까지 혹은 끝날때까지
right_leg=0
for i in range(head_x+2+core,N):
    if maps[i][head_y+1]=="*":
        right_leg+=1
result.append(right_leg)      
print(head_x+2,head_y+1)
print(*result)