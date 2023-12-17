def solution(numbers):
    answer = 0
    numbers.sort()
    
    max_list = []
    
    max_list.append(numbers[0] * numbers[1])
    max_list.append(numbers[-2] * numbers[-1])
    answer = max(max_list)
    return answer