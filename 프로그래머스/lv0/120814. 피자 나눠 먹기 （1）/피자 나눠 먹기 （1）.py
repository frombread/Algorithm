def solution(n):
    if n % 7!=0:
        answer = (n // 7) + 1
    elif n % 7==0:
        answer = (n/7)  
        
        
        
    # while 7 % n !=0:
    #     if 7 % n == 1:
    #         break
    #     n += 1
    #     answer +=1
    return answer