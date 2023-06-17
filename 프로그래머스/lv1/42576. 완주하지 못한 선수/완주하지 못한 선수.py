from collections import deque
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    completion.append(-1)
    for i, j in zip(participant,completion):
        if i != j:
            return(i)

    
    
    