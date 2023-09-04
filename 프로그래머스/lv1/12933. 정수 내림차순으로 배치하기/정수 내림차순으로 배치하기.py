def solution(n):
    answer = 0
    n = str(n)
    n_list = list(n)

    sort_list = sorted(n_list,reverse=True)
    answer = int(''.join(sort_list))
    return answer