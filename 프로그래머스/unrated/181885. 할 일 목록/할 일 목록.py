def solution(todo_list, finished):
    answer = []
    for i,j in zip(todo_list,finished):
        if j !=True:
            answer.append(i)
    return answer