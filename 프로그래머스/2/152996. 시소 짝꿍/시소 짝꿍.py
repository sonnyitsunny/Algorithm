from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    # 1:1 (같은 무게)
    for w in counter:
        if counter[w] >= 2:
            answer += counter[w] * (counter[w] - 1) // 2  # ★ 조합식 수정
    
    # 3:2, 2:1, 4:3
    for w in counter:
        # 3:2 비율 → w * 3 / 2
        if (w * 3) % 2 == 0:               # 정수인지 체크
            t = (w * 3) // 2              # float 말고 정수 연산
            if t in counter:
                answer += counter[w] * counter[t]

        # 2:1 비율 → w * 2
        t = w * 2
        if t in counter:
            answer += counter[w] * counter[t]

        # 4:3 비율 → w * 4 / 3
        if (w * 4) % 3 == 0:               # 정수인지 체크
            t = (w * 4) // 3
            if t in counter:
                answer += counter[w] * counter[t]
    
    return answer
