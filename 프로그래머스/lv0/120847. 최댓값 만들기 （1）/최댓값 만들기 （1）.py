def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers.pop()
    b = numbers.pop()
    answer = a*b
    return answer