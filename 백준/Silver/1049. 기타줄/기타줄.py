import sys
input = sys.stdin.readline

# 6개짜리 패키지 가격, 1개짜리 가격
# 패키지 + 낱개 도 가능
# 조합은 다른 브랜드 섞어서 구매 가능함

#끊어진 줄을 6으로 나누고 그 몫을 (패키지,낱개*6)중에 제일 작은거와와 곱한다. 그리고 나머지는 (낱개 *개수,젤작은패키지)중에 작은 걸 고른다.

N,M=map(int,input().split())
mix=[]#배열1 = 패키지+낱개*6
one=[]#배열2 = 낱개만 있는거 
pack=[]#배열3 = 패키지만 있는거

for _ in range(M):
    p,o=map(int,input().split())
    mix.append(p)
    mix.append(o*6)
    one.append(o)
    pack.append(p)

mix.sort()
one.sort()
pack.sort()

cost=0
p_cnt=N//6
o_cnt=N%6

cost+=p_cnt*mix[0]
cost+=min(o_cnt*one[0],pack[0])
print(cost)