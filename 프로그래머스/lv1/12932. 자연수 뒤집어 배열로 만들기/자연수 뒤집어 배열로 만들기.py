def solution(n):
    answer = []
    list_ = list(str(n))
    for i in range(len(list_)-1,-1,-1):
        answer.append(int(list_[i]))
    return answer