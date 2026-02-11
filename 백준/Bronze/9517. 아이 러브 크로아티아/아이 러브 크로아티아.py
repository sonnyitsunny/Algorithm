K=int(input())
N=int(input())

time=0

questions=[]
for _ in range(N):
    t,q=input().split()
    questions.append((int(t),q))

for t,q in questions:

    if q=="T":
        time+=t
        if time<210:
            K=(K%8)+1
        else:
            print(K)
            break
    else:
        time+=t
        if time<210:
            continue
        else:
            print(K)
            break