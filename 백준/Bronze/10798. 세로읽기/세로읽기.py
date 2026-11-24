

arr=[]
max_len=0
for _ in range(5):
    w = input()
    arr.append(w)
    max_len=max(max_len, len(w))


for i in range(5):
    words=arr[i]
    if len(words)<max_len:
        cnt = max_len - len(words)
        plus='@'*cnt
        arr[i]=words+plus

res=""
for j in range(max_len):
    for i in range(5):
        if arr[i][j]!="@":
            res+=arr[i][j]
print(res)