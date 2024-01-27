def solution(my_string, is_suffix):
    answer = 0
    my_string_list = list(my_string)
    for i in range(len(my_string_list)):
        if ''.join(my_string_list[i::]) == is_suffix:
            return 1
    return answer