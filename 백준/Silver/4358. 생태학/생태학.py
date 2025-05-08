import sys

from collections import defaultdict
hash=defaultdict(int)
cnt=0

for line in sys.stdin:
    word = line.strip()  
    if not word:
        continue
    hash[word] += 1
    cnt += 1

trees=sorted(hash.items(),key=lambda x:(x[0],-x[1]))
for k,v in trees:
    ratio=v/cnt*100
    print(f"{k} {ratio:.4f}")