def solution(num_list):
    compare_list = num_list[-2:]
    
    if compare_list[0]>= compare_list[1]:
        num_list.append(compare_list[1]*2)
    elif compare_list[0]< compare_list[1]:
        num_list.append(compare_list[1]-compare_list[0])
    
    return num_list