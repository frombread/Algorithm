def solution(array, commands):
    answer = []
    for i in commands:
        list_1= []
        list_1 = array[i[0]-1:i[1]]
        list_1.sort()
        answer.append(list_1[i[2]-1])
    return answer