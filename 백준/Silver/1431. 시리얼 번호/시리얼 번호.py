n=int(input())
serials=[]
for _ in range(n):
    serials.append(input())



def d_sum(x):
    d=0
    for i in x:
        if i.isdigit():
            d+=int(i)


    return d

serials.sort(key=lambda x: (len(x),d_sum(x),x))

for word in serials:
    print(word)