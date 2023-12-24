def solution(array):
    answer =[0]*2
    for i in range(len(array)):
        if array[i]>= answer[0]:
            answer[0] = array[i]
            answer[1] = i
    return answer