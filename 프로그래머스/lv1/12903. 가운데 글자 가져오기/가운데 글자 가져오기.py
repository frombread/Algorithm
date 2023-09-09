def solution(s):
    res = list(s)
    answer = ''
    if len(res) %2== 0:
        answer = str(res[(len(res)//2)-1]) + str(res[len(res)//2])
    else:
        answer = str(res[len(res)//2])

    return answer