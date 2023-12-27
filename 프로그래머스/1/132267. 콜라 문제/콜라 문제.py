def solution(a, b, n):
    answer = 0
    re = 0
    while n>=a:
        answer+= n//a * b
        n = (n//a*b) +round(n%a)        
    return answer

