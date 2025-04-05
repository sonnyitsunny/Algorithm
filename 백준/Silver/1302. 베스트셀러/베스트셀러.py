n=int(input())

books={}
for _ in range(n):
    name=input()

    if name in books:
        books[name]+=1
    else:
        books[name]=1

best=list(books.items())
best.sort(key=lambda x:(-x[1],x[0]))
print(best[0][0])