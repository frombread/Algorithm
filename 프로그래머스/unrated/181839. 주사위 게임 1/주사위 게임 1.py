def solution(a, b):
    answer = 0
    if a %2 ==1 and b%2 ==1:
        answer = a**2 + b**2
    elif a%2 ==1 or b%2==1:
        answer = 2*(a+b)
    else:
        if a>b :
            answer = a-b
        else:
            answer = b-a
        
    return answer