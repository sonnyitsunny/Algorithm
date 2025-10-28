def solution(n, words):
    answer = [0,0]

    # %인원수 해주고 +1해야 그사람 번호임
    # 차례는 //인원수를 구하고 +1 하면됨
        
   
    already=set()
    last_word=""
    for i in range(len(words)):
        start_word=words[i][0]
        
        if words[i] in already:
            answer=[i%n+1,i//n+1]
            break
        elif i>=1 and start_word!=last_word:
            answer=[i%n+1,i//n+1]
            break
        else:
            already.add(words[i])
            last_word=words[i][-1]
        
        


    return answer