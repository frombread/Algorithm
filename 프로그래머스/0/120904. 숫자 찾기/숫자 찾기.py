def solution(num, k):
    answer = -1
    num1 = list(str(num))
    for i in range(len(num1)):
        if num1[i] == str(k):
            return i+1
    return answer