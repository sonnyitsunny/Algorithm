
s,p=map(int,input().split())
dna=input()
a,c,g,t=map(int,input().split())

cnt=0
    
cnt_a=0
cnt_c=0
cnt_g=0
cnt_t=0

for i in range(p):
    if dna[i]=='A':
        cnt_a+=1
    elif dna[i]=='C':
        cnt_c+=1
    elif dna[i]=='G':
        cnt_g+=1
    elif dna[i]=='T':
        cnt_t+=1
if cnt_a>=a and cnt_c>=c and cnt_g>=g and cnt_t>=t:
    cnt+=1


for i in range(p, s):

    if dna[i] == 'A':
        cnt_a += 1
    elif dna[i] == 'C':
        cnt_c += 1
    elif dna[i] == 'G':
        cnt_g += 1
    elif dna[i] == 'T':
        cnt_t += 1

    out = dna[i - p]
    if out == 'A':
        cnt_a -= 1
    elif out == 'C':
        cnt_c -= 1
    elif out == 'G':
        cnt_g -= 1
    elif out == 'T':
        cnt_t -= 1


    if cnt_a >= a and cnt_c >= c and cnt_g >= g and cnt_t >= t:
        cnt += 1
print(cnt)