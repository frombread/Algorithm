def solution(k, m, score):
    score.sort()
    answer = 0
    while len(score) >= m:
        result =[]
        for _ in range(m):
            add_fruit = score.pop()
            result.append(add_fruit)
    
        answer += (min(result) * m)
    return answer