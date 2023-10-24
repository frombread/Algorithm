def solution(num_list):
    answer = 0
    a =""
    b= ""
    for i in num_list:
        if i %2 ==0:
            a+=str(i)
        else:
            b+=str(i)
    print(a,b)
    answer = int(a)+int(b)
    return answer