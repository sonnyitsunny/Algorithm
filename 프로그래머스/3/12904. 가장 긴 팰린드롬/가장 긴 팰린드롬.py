def solution(s):
    n = len(s)
    answer = 1

    for center in range(n):
        # 홀수 중심
        left, right = center - 1, center + 1
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1

        # 짝수 중심
        left, right = center, center + 1
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1

    return answer
