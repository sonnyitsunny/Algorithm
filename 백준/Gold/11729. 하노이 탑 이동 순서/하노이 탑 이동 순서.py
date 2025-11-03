import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n=int(input())
moves=[]


def hanoi(n,a,b):
    if n==1:
        moves.append((a,b))
        return
    
    hanoi(n-1,a,6-a-b)
    moves.append((a,b))
    hanoi(n-1,6-a-b,b)

hanoi(n,1,3)

print(len(moves))
for a,b in moves:
    print(a,b)