from collections import defaultdict
def solution(participant, completion):
    answer = ''
    player=defaultdict(int)
    for p in participant:
        player[p]+=1
    for c in completion:
        player[c]-=1
    
    sorted_player = sorted(player.items(),key=lambda x:-x[1])
    
    answer = sorted_player[0][0]
    return answer