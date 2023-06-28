from collections import deque
def solution(people, limit):
    answer = 0
    wei=0
    q = deque()
    people.sort(reverse = 1)
    for i in people:
        q.append(i)
    while q:
        M_num = q.popleft()
        wei += M_num
        while wei < limit and q:
            m_num = q.pop()
            if wei + m_num >limit:
                q.append(m_num)
                break
            else:
                wei += m_num
        wei =0
        answer +=1
        
    return answer