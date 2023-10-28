def solution(n, k):
    answer = []
    for i in range(1,10000):
        if k*i <= n:
            answer.append(k*i)
        else:
            break
    return answer