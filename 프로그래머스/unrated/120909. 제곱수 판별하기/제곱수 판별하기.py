def solution(n):
    answer = 0
    for i in range(n//2):
        if i**2 == n:
            answer = i
    if answer ==0:
        return 2
    return 1