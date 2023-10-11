from collections import deque
def solution(s):
    answer = ""
    str_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_list =["0","1","2","3","4","5","6","7","8","9"]
    q = deque(list(s))
    str_=""
    while q:
        a = q.popleft()
        if a in num_list:
            answer+=a
        else:
            str_+=a
        for i in range(10):
            if str_ == str_list[i]:
                answer+=str(i)
                str_=""
                break
    return int(answer)