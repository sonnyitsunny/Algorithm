import sys
input=sys.stdin.readline

score1=0
score2=0

lead1=0
lead2=0

prev_time=0
leader=0


n=int(input())

def time_to_sec(t):
    m,s=map(int,t.split(":"))
    return m*60+s


def sec_to_time(sec):
    m=sec//60
    s=sec%60
    return f"{m:02d}:{s:02d}"



for _ in range(n):
    team,t=input().split()
    team=int(team)
    cur_time=time_to_sec(t)

    if leader==1:
        lead1+=cur_time-prev_time
    
    elif leader==2:
        lead2+=cur_time-prev_time

    if team == 1:
        score1+=1

    else:
        score2+=1

    if score1>score2:
        leader=1
    elif score2>score1:
        leader=2
    else:
        leader=0

    prev_time=cur_time
end_time=48*60
if leader==1:
    lead1+=end_time-prev_time
elif leader==2:
    lead2+=end_time-prev_time
print(sec_to_time(lead1))
print(sec_to_time(lead2))