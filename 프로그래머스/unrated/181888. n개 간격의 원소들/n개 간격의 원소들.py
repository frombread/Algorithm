def solution(num_list, n):
    answer = []
    cnt =0
    while cnt <= len(num_list):
        if cnt >= len(num_list):
            break
        answer.append(num_list[cnt])
        cnt+=n
    return answer