from collections import defaultdict
n,m=map(int,input().split())
hash={}
#n부터 m까지 하고 문자열로 바꿔서 

#0~9
number=['zero','one','two','three','four','five','six','seven','eight','nine']

for num in range(n,m+1):
    #한자리수
    if len(str(num))==1:
        first=number[num]
        hash[num]=first



    # 두자리 수
    else:
        first=number[num//10]
        second=number[num%10]
        hash[num]=first+second

sorted_hash=sorted(hash.items(),key=lambda x : x[1])

only_first = [x[0] for x in sorted_hash]
for i in range(0,len(only_first),10):
    print(*only_first[i:i+10])
