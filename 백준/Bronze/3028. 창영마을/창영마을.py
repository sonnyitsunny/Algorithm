seq=list(input())
ball=1

for s in seq:
    if s=='A':
        if ball==1:
            ball=2
        elif ball==2:
            ball=1

    elif s=='B':
        if ball==2:
            ball=3
        elif ball==3:
            ball=2

    else:
        if ball == 1:
            ball=3
        elif ball == 3:
            ball=1
print(ball)