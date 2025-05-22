from collections import defaultdict
a = input().strip()
b = input().strip()

da=defaultdict(int)
db=defaultdict(int)
for ch in a:
    da[ch]+=1

for ch in b:
    db[ch]+=1


total=0

for k in da.keys()|db.keys():
    total+=abs(da[k]-db[k])
print(total)