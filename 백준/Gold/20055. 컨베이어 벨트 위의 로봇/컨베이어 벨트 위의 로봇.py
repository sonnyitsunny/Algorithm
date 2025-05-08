#n,k를 받는다
#1차원 배열을 만들고 입력을 넣는다
#2차원 배열을 만든다.(벨트)
#2차원 배열 만든다.(로봇)
#n-1인덱스 까지는 2차원의 0번에 n인덱스부터는 2차원의 1번에(역순으로)

#step=0 (단계 따지기)
#cnt=0 (내구도 0인 칸 수)
import sys
input = sys.stdin.readline

n,k=map(int,input().split())
values=list(map(int,input().split()))

belt=[[0]*n for _ in range(2)]
robot=[False]*n 

for i in range(n):
    belt[0][i]=values[i]
reverse=values[n:]
reverse=reverse[::-1]
for i in range(n):
    belt[1][i]=reverse[i]

step=0
cnt=0

#반복문
#1.벨트회전하고 내구도 깎기, 근데 그위에 로봇이 있으니까 로봇은 위치만 회전시켜준다.
#2. 로봇 있는지 확인하고 로봇이동시켜주기(조건을 따져야함)
#3.로봇올리기(조건따져야함)
#4. 내구도 0인칸 갯수 확인 k랑비교

def rotation1():
    end=belt[0][n-1]
    start=belt[1][0]

    for i in range(n-2,-1,-1):
        belt[0][i+1]=belt[0][i]
    
    for i in range(1,n):
        belt[1][i-1]=belt[1][i]
    belt[1][n-1]=end
    belt[0][0]=start

def rotation2():
    for i in range(n-2,-1,-1):
        robot[i+1]=robot[i]
    robot[0]=False
    robot[n-1]=False


def move():
    for i in range(n-2,-1,-1):
        if not robot[i+1] and robot[i] and belt[0][i+1]>=1:
            robot[i+1]=robot[i]
            robot[i]=False
            belt[0][i+1]-=1
    robot[n-1]=False
    

def check():
    global cnt
    cnt=0
    for i in range(2):
        for j in range(n):
            if belt[i][j]==0:
                cnt+=1
    if cnt>=k:
        return True
    else:
        return False
    
while True:
    #회전 + 내구도 깎기
    step+=1
    rotation1()
    rotation2()

    move()

    if belt[0][0]!=0:
        robot[0]=True
        belt[0][0]-=1


    if check():
        break  
    

print(step)