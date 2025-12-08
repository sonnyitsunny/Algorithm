import sys
input = sys.stdin.readline

N, K = map(int, input().split())


base = {'a', 'n', 't', 'i', 'c'}

if K < 5:
    print(0)
    exit()

words = []
cand = set()   

for _ in range(N):
    s = input().strip()
    mid = set(s[4:-4])  
    # 각 단어의 가운데 글자들 저장
    words.append(mid)

   
    for ch in mid:
        if ch not in base:
            cand.add(ch)

need = K - 5   

if len(cand) <= need:
    print(N)
    exit()

#  그렇지 않다면  백트래킹 진행
cand_list = list(cand)
answer = 0

learned = set(base)

def dfs(idx, count):
    global answer

   
    if count == need:
        cnt = 0
        for w in words:
            if w.issubset(learned):
                cnt += 1
        answer = max(answer, cnt)
        return

    if idx == len(cand_list):
        return

   
    learned.add(cand_list[idx])
    dfs(idx + 1, count + 1)
    learned.remove(cand_list[idx])

    
    dfs(idx + 1, count)

dfs(0, 0)
print(answer)
