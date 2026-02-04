A,B,C,M=map(int,input().split())

time=24
work=0
bad=0

while time>0:
    if bad==0 and bad+A>M:
        break

    if bad+A>M and bad>0:
        time-=1
        bad-=C
        if bad<0:
            bad=0

        continue
    work+=B
    time-=1
    bad+=A

print(work)