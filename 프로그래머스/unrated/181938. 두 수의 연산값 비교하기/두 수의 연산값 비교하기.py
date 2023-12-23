def solution(a, b):
    answer = []
    answer.append(2*a*b)
    answer.append(int(str(a)+str(b)))
    return max(answer)