def solution(my_string):
    answer = ''
    list_ = ['a','e','i','o','u']
    
    for i in my_string:
        if i not in list_:
            answer += i
    return answer