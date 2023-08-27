def solution(my_string):
    answer = ''
    woo = list(my_string)
    for i in range(len(woo)-1,-1,-1):
        answer += str(woo[i])
    return answer