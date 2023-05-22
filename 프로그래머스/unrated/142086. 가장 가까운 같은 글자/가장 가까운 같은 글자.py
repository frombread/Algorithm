def solution(s):
    word_len = len(s)
    answer = [-1]*(word_len)
    for point_1 in range(word_len-1,0,-1):
        for point_2 in range(point_1-1, -1,-1):
            if s[point_1] == s[point_2]:
                answer[point_1]=point_1-point_2
                break
    return answer
