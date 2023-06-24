def solution(s):
    list1=list(map(int,s.split()))
    a,b= str(min(list1)),str(max(list1))
    answer = a+" "+b
    return answer