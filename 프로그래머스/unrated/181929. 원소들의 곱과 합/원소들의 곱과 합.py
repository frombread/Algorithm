def solution(num_list):
    answer = 1
    answer2=0
    for i in num_list:
        answer2+=i
        answer*=i
        
    print(answer,answer2**2)
    if answer<(answer2**2):
        
        return 1
    return 0