from collections import deque
def solution(arr):
    q = deque(arr)
    answer = []
    while q:
        a = q.popleft()
        if len(answer)==0:
            answer.append(a)
        else:
            if answer[-1] !=a:
                answer.append(a)
    
    return answer